# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import math
import fractions 
class Stack(object):
	def __init__(self, limit=10):
		self.stk = []
		self.limit = limit	
	def isEmpty(self):
		return len(self.stk) <= 0

	def push(self, item):
		if len(self.stk) >= self.limit:
			print 'Stack Overflow!'
		else:
			self.stk.append(item)
		print 'Stack after Push', self.stk

	def pop(self):
		if len(self.stk) <= 0:
			print 'Stack Underflow!'
			return 0
		else:
			return self.stk.pop()
			
	def peek(self):
		if len(self.stk) <= 0:
			print 'Stack Underflow!'
			return 0
		else:
			return self.stk[-1]
			
	def size(self):
		return len(self.stk)

# Node of a Singly Linked List
class Node:
	# constructor
	def __init__(self, data=None, next=None):
		self.data = data
		self.last = None
		self.next = next
	# method for setting the data field of the node    
	def set_data(self, data):
		self.data = data
	# method for getting the data field of the node   
	def get_data(self):
		return self.data
	# method for setting the next field of the node
	def set_next(self, next):
		self.next = next
	# method for getting the next field of the node    
	def get_next(self):
		return self.next
	# method for setting the last field of the node
	def setLast(self, last):
		self.last = last
	# method for getting the last field of the node    
	def getLast(self):
		return self.last	
	# returns true if the node points to another node
	def has_next(self):
		return self.next != None


class Queue(object):
	def __init__(self, data=None):
		self.front = None
		self.rear = None
		self.size = 0

	def enQueue(self, data):
		self.lastNode = self.front
		self.front = Node(data, self.front)
		if self.lastNode:
			self.lastNode.setLast(self.front)
		if self.rear is None:
			self.rear = self.front
		self.size += 1

	def queueRear(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.rear.get_data()

	def queueFront(self):
		if self.front is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.front.get_data()

	def deQueue(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		result = self.rear.get_data()
		self.rear = self.rear.last
		self.size -= 1
		return result

	def size(self):
		return self.size
		
	def isEmpty(self):
		return self.size == 0			
  
def interLeavingQueue(que):
     stk = Stack()
     halfSize = que.size // 2
     for i in range(0, halfSize):
          stk.push(que.deQueue())
     while not stk.isEmpty():
          que.enQueue(stk.pop())
     for i in range(0, halfSize):
          que.enQueue(que.deQueue())
     for i in range(0, halfSize):
          stk.push(que.deQueue())
     while not stk.isEmpty():
          que.enQueue(stk.pop())
          que.enQueue(que.deQueue())
	  
que = Queue()
que.enQueue(11)
que.enQueue(12)
que.enQueue(13)
que.enQueue(14)
que.enQueue(15)
que.enQueue(16)
que.enQueue(17)
que.enQueue(18)
que.enQueue(19)
que.enQueue(20)
que.enQueue(21)
que.enQueue(22)

interLeavingQueue(que)	  

while not que.isEmpty():
    print que.deQueue()   
