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
        self.data = data
        self.next = None
         
    def set_data(self, data):
        self.data = data
     
    def get_data(self):
        return self.data
     
    def set_next(self, next):
        self.next = next
         
    def get_next(self):
        return self.next
     
     
class LinkedList:
    def __init__(self):
        self.head = None
	
    def modularNodeFromBegin(self, k):
		currentNode = self.head
		modularNode = None
		i = 1
		if k <= 0:
			return None;
		while currentNode != None:
			if i % k == 0:
				modularNode = currentNode		
			i = i + 1
			currentNode = currentNode.get_next()
		print (modularNode.get_data())
		
    def modular_node_from_end(self, k):
		currentNode = self.head
		modularNode = self.head
		i = 1
		if k <= 0:
			return None;
		
		while i < k and currentNode != None:
			i = i + 1
			currentNode = currentNode.get_next()
		
		if currentNode == None:
			return
		while currentNode != None:
			modularNode = modularNode.get_next()		
			currentNode = currentNode.get_next()

		print (modularNode.get_data())
			
    def insertAtEnd(self, item):
        current = self.head
        if  current == None:
            node = Node(item)
            node.set_next(None)
            self.head = node
            return
            
        while current.get_next() != None:
            current = current.get_next()
             
        node = Node(item)
        current.set_next(node)

if __name__ == "__main__":
    linkedlst = LinkedList()
    linkedlst.insertAtEnd(1)
    linkedlst.insertAtEnd(2)
    linkedlst.insertAtEnd(3)
    linkedlst.insertAtEnd(4)
    linkedlst.modular_node_from_end(4)
