# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

from Queue import Queue

import threading
import random
import time

class ProduceToQueue(threading.Thread):
   def __init__(self, threadName, queue):
      threading.Thread.__init__(self, name=threadName)
      self.sharedObject = queue
      
   def run(self):
      for i in range(11, 21):
         time.sleep(random.randrange(4))
         print "%s adding %s to queue" % (self.getName(), i)
         self.sharedObject.put(i)

      print self.getName(), "finished producing values"
      print "Terminating", self.getName()

class ConsumeFromQueue(threading.Thread):
   def __init__(self, threadName, queue):
      threading.Thread.__init__(self, name=threadName)
      self.sharedObject = queue

   def run(self):
      sum = 0
      current = 10

      for i in range(10):
         time.sleep(random.randrange(4))
         print "%s attempting to read %s..." % (self.getName(), current + 1)
         current = self.sharedObject.get()
         print "%s read %s" % (self.getName(), current)
         sum += current

      print "%s retrieved values totaling: %d" % (self.getName(), sum)
      print "Terminating", self.getName()

queue = Queue()
producer = ProduceToQueue("Producer", queue)
consumer = ConsumeFromQueue("Consumer", queue)

producer.start()
consumer.start()

producer.join()
consumer.join()
