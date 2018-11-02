import Semaphore
import ChopStick
import Philosopher

def main():

    forks = 5
    semaphore = Semaphore(forks-1)
    chopsticks = [ChopStick(fork) for fork in range(forks)]
    philosophers = [Philosopher(fork, chopsticks[fork], chopsticks[(fork+1)%forks], semaphore) for fork in range(forks)]
    for fork in range(forks):
        philosophers[fork].start()
  if __name__ == "__main__":
    main()
