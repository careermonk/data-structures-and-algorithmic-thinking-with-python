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
	def __init__(self): 
		self.queue = [] 
		
	def isEmpty(self): 
		return self.queue == [] 
		
	def enqueue(self, x): 
		self.queue.append(x) 
		
	def dequeue(self): 
		if self.queue: 
			a = self.queue[0] 
			self.queue.remove(a) 
			return a 
		else: 
			raise IndexError, 'queue is empty' 
			
	def size(self): 
		return len(self.queue) 

class Stack(object): 
	def __init__(self): 
		self.Q1 = Queue() 
		self.Q2 = Queue() 
		
	def isEmpty(self): 
		return self.Q1.isEmpty() and self.Q2.isEmpty() 
		
	def push(self, item): 
		if self.Q2.isEmpty(): 
			self.Q1.enqueue(item) 
		else: 
			self.Q2.enqueue(item) 
			
	def pop(self): 
		if self.isEmpty(): 
			raise IndexError, 'stack is empty' 
		elif self.Q2.isEmpty(): 
			while not self.Q1.isEmpty(): 
				cur = self.Q1.dequeue() 
				if self.Q1.isEmpty(): 
					return cur 
				self.Q2.enqueue(cur) 
		else: 
			while not self.Q2.isEmpty(): 
				cur = self.Q2.dequeue() 
				if self.Q2.isEmpty(): 
					return cur 
				self.Q1.enqueue(cur)

s = Stack()
for i in xrange(5):
    s.push(i)
for i in xrange(5):
    print s.pop()  
