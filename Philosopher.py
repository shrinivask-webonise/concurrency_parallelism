import sys
import threading
import time

class Philosopher (threading.Thread):

  def __init__(self, number, left, right, semaphore):
	threading.Thread.__init__(self)
	self.number = number
	self.left = left
	self.right = right
	self.semaphore = semaphore

  def run(self):
    max_range=20;
	time_ml=1000
    for philosopher in range(max_range):
	  self.semaphore.down()
	  time.sleep(time_ml)
	  self.left.take(self.number)
	  time.sleep(time_ml)
	  self.right.take(self.number)
	  time.sleep(time_ml)
	  self.right.drop(self.number)
	  self.left.drop(self.number)
	  self.semaphore.up()
	  sys.stdout.write("Philosopher[%s] finished thinking and eating\n" % self.number)
