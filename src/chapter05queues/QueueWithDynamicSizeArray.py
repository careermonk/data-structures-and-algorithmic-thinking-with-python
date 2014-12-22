# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class Queue(object):
	def __init__(self, limit=5):
		self.que = []
		self.limit = limit
		self.front = None
		self.rear = None
		self.size = 0		

	def isEmpty(self):
		return self.size <= 0

	def enQueue(self, item):
		if self.size >= self.limit:
			self.resize()

		self.que.append(item)
			
		if self.front is None:	
			self.front = self.rear = 0
		else:
			self.rear = self.size
		self.size += 1
		print 'Queue after enQueue', self.que
		
	def deQueue(self):
		if self.size <= 0:
			print 'Queue Underflow!'
			return 0
		else:
			self.que.pop(0)
			self.size -= 1
			if self.size == 0:
				self.front = self.rear = None	
			else:
				self.rear = self.size - 1
			print 'Queue after deQueue', self.que
			
	def queueRear(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.que[self.rear]

	def queueFront(self):
		if self.front is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.que[self.front]
			
	def size(self):
		return self.size

	def resize(self):
		newQue = list(self.que)
		self.limit = 2 * self.limit 
		self.que = newQue

que = Queue()
que.enQueue("first")
print "Front: " + que.queueFront()
print "Rear: " + que.queueRear()
que.enQueue("second")
print "Front: " + que.queueFront()
print "Rear: " + que.queueRear()
que.enQueue("third")
print "Front: " + que.queueFront()
print "Rear: " + que.queueRear()
que.enQueue("four")
print "Front: " + que.queueFront()
print "Rear: " + que.queueRear()
que.enQueue("five")
print "Front: " + que.queueFront()
print "Rear: " + que.queueRear()
que.enQueue("six")
print "Front: " + que.queueFront()
print "Rear: " + que.queueRear()
que.deQueue()
print "Front: " + que.queueFront()
print "Rear: " + que.queueRear()
que.deQueue()
print "Front: " + que.queueFront()
print "Rear: " + que.queueRear()
