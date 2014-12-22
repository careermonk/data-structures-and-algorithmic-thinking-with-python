# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

#!/usr/bin/env python

from random import randint
from time import sleep
from Queue import Queue
from myThread import MyThread

def writeQ(queue):
	print 'producing object for Q...',
	queue.put('MONK', 1)
	print "size now", queue.qsize()

def readQ(queue):
	val = queue.get(1)
	print 'consumed object from Q... size now', queue.qsize()

def producer(queue, loops):
	for i in range(loops):
	   writeQ(queue)
	   sleep(randint(1, 3))

def consumer(queue, loops):
	for i in range(loops):
	   readQ(queue)
	   sleep(randint(2, 5))

funcs = [producer, consumer]
nfuncs = range(len(funcs))

nloops = randint(2, 5)
q = Queue(32)

threads = []
for i in nfuncs:
   t = MyThread(funcs[i], (q, nloops),
       funcs[i].__name__)
   threads.append(t)

for i in nfuncs:
   threads[i].start()

for i in nfuncs:
   threads[i].join()

print 'all DONE'
