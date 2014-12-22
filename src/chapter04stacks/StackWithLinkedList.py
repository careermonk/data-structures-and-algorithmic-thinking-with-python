# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Node of a Singly Linked List
class Node:
    # constructor
    def __init__(self):
        self.data = None
        self.next = None
        # method for setting the data field of the node    
    def setData(self, data):
        self.data = data
    # method for getting the data field of the node   
    def getData(self):
        return self.data
      # method for setting the next field of the node
    def setNext(self, next):
        self.next = next
       # method for getting the next field of the node    
    def getNext(self):
        return self.next
    # returns true if the node points to another node
    def hasNext(self):
            return self.next != None
	    
class Stack(object):
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.getData()
        self.head = self.head.getNext()
        return temp
	
    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.getData()


our_list = ["first", "second", "third", "fourth"]
our_stack = Stack(our_list)
print our_stack.pop()
print our_stack.peek()
print our_stack.pop()
print our_stack.peek()
print our_stack.pop()
