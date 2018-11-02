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
