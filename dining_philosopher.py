
import sys
import threading
import time

class Semaphore(object):

    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1

class ChopStick(object):

    def __init__(self, number):
        self.number = number
        self.user = -1
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write("Philosopher[%s] took ChopStick[%s]\n" % (user, self.number))
            self.lock.notifyAll()

    def drop(self, user):
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            sys.stdout.write("Philosopher[%s] put down ChopStick[%s]\n" % (user, self.number))
            self.lock.notifyAll()


class Philosopher (threading.Thread):

    def __init__(self, number, left, right, semaphore):
        threading.Thread.__init__(self)
        self.number = number
        self.left = left
        self.right = right
        self.semaphore = semaphore

    def run(self):
        for i in range(20):
            self.semaphore.down()
            time.sleep(0.1)
            self.left.take(self.number)
            time.sleep(0.1)
            self.right.take(self.number)
            time.sleep(0.1)
            self.right.drop(self.number)
            self.left.drop(self.number)
            self.semaphore.up()
        sys.stdout.write("Philosopher[%s] finished thinking and eating\n" % self.number)


def main():

    forks = 5


    semaphore = Semaphore(forks-1)


    chopsticks = [ChopStick(i) for i in range(forks)]


    philosophers = [Philosopher(i, chopsticks[i], chopsticks[(i+1)%forks], semaphore) for i in range(forks)]

    for i in range(forks):
        philosophers[i].start()


if __name__ == "__main__":
    main()
