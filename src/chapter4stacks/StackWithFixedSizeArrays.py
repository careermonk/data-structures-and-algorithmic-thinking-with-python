# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

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
	 

our_stack = Stack(5)
our_stack.push("1")
our_stack.push("21")
our_stack.push("14")
our_stack.push("11")
our_stack.push("31")
our_stack.push("14")
our_stack.push("15")
our_stack.push("19")
our_stack.push("3")
our_stack.push("99")
our_stack.push("9")
print our_stack.peek()
print our_stack.pop()
print our_stack.peek()
print our_stack.pop()
