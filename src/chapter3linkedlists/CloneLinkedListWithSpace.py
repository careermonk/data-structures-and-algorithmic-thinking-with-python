# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class Node:
	def __init__(self, data):
		self.setData(data)
		self.setNext(None)
		self.setRand(None)
	# method for setting the data field of the node    
	def setData(self, data):
		self.data = data
	# method for getting the data field of the node   
	def getData(self):
		return self.data
	# method for setting the next field of the node
	def setNext(self, next):
		self.next = next
	# method for setting the next field of the node
	def setRand(self, rand):
		self.rand = rand	
	# method for getting the next field of the node
	def getRand(self):
		return self.rand	
	# method for getting the next field of the node    
	def getNext(self):
		return self.next
	# returns true if the node points to another node
	def hasNext(self):
	    return self.next != None
	    
	def cloneLinkedList(old):
	    if not old:
		return

	    old_copy = old
	    root = Node(old.getData())
	    prev = root
	    temp = None

	    old = old.getNext()

	    mapping = {}
	    
	    while old:
		temp = Node(old.getData())
		mapping[old] = temp
		
		prev.setNext(temp)
		prev = temp
		old = old.getNext()

	    old = old_copy
	    temp = root

	    while old:
		temp.setRand(mapping[old.rand])
		temp = temp.getNext()
		old = old.getNext()

	    return root
