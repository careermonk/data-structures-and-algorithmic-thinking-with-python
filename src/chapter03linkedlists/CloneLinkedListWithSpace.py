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
		self.set_data(data)
		self.set_next(None)
		self.set_rand(None)
	# method for setting the data field of the node    
	def set_data(self, data):
		self.data = data
	# method for getting the data field of the node   
	def get_data(self):
		return self.data
	# method for setting the next field of the node
	def set_next(self, nextV):
		self.next = nextV
	# method for setting the next field of the node
	def set_rand(self, rand):
		self.rand = rand	
	# method for getting the next field of the node
	def get_rand(self):
		return self.rand	
	# method for getting the next field of the node    
	def get_next(self):
		return self.next
	# returns true if the node points to another node
	def has_next(self):
	    return self.next != None
	    
	def clone_linked_list(old):
	    if not old:
		return

	    old_copy = old
	    root = Node(old.get_data())
	    prev = root
	    temp = None

	    old = old.get_next()

	    mapping = {}
	    
	    while old:
		temp = Node(old.get_data())
		mapping[old] = temp
		
		prev.set_next(temp)
		prev = temp
		old = old.get_next()

	    old = old_copy
	    temp = root

	    while old:
		temp.set_rand(mapping[old.rand])
		temp = temp.get_next()
		old = old.get_next()

	    return root
