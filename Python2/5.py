import os
import thread
import time
import random
import threading

class Philosopher:
  def __init__(self, id, fork1, fork2):
    self.fork1=fork1
    self.fork2=fork2
    self.id=id
  def start(self):
    while True:
      time.sleep(random.randint(0,4))
      if self.fork1.acquire(False):
        if self.fork2.acquire(False):
          print "Philosopher {} is eating".format(self.id)
          time.sleep(random.randint(0,4))
          print "Philosopher {} finished".format(self.id)
          self.fork1.release()
          self.fork2.release()
        else:
          self.fork1.release()

           
          
if(__name__ == "__main__"):
  numOfPhil=5
  forks=[threading.Lock() for i in xrange(numOfPhil)]
  philos=[Philosopher(i,forks[i],forks[(i+1)%numOfPhil]) for i in xrange(numOfPhil)]
  for phi in philos:  
    thread.start_new_thread(phi.start,())
  time.sleep(60)

