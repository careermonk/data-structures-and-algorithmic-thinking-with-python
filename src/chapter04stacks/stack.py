# Copyright (c) Oct 22, 2018 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import random 

class Stack:
	def __init__(self, C = 5):
		self.C = C
		self.array = []
	def size(self):
		return len(self.array)
	def isEmpty(self):
		return len(self.array) == 0
	def isFull(self):
		return len(self.array) == self.C
	def peek(self):
		if self.isEmpty():
			return None
		return self.array[self.size()-1]
	def pop(self):
		if self.isEmpty():
			print "Underflow"
			return None
		data = self.array.pop()
		return data
	def push(self, data):
		if self.isFull():
			print "Overflow"
			return
		self.array.append(data)

def testStack(stackCap):
	stack = Stack(stackCap)
	c = stackCap * 2
	while(c):
		data = random.randrange(1,100)
		print "Pushing ", data
		stack.push(data)
		c -= 1
	print "Stack size ", stack.size()
	c = stackCap * 2
	while(c):
		print "Popping", stack.pop()
		c -= 1

print testStack(6)
