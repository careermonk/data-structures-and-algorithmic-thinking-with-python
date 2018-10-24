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

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    def enqueue(self, data):
        self.s1.push(data)

    def dequeue(self):
		if (not self.s2.isEmpty()):
			return self.s2.pop()
		while(not self.s1.isEmpty()):
			self.s2.push(self.s1.pop())
		return self.s2.pop()

q = Queue()
q.enqueue(1)
q.enqueue(6)
q.enqueue(8)
q.enqueue(10)
q.enqueue(16)
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
