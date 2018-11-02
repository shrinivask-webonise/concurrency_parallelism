import sys
import threading
import time

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
