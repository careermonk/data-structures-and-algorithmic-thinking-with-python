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
    
    def recursiveReverseList(self) :
		self.reverseRecursive(self.head)
		
    def reverseRecursive(self, n) :
		if None != n:
			right = n.get_next()
			if self.head != n:
				n.set_next(self.head)
				self.head = n
			else:
				n.set_next(None)
			self.reverseRecursive(right)
			
    def printListFromEnd(self, list) :
    	if list == None: 
    		return
    	head = list
    	tail = list.get_next()
    	self.printListFromEnd(tail)
    	print head.get_data(), 	

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
         
    def printList(self):
        current = self.head
         
        while current != None:
            print current.get_data()
            current = current.get_next()
    
    def isLinkedListLengthEven(self):
        current = self.head
         
        while current != None and current.get_next() != None:
            current = current.get_next().get_next()  
	    
	if current == None:
		return 1
	return 0	

if __name__ == "__main__":
    linkedlst = LinkedList()
    linkedlst.insertAtEnd(1)
    linkedlst.insertAtEnd(2)
    linkedlst.insertAtEnd(3)
    linkedlst.insertAtEnd(4)
     
    linkedlst.printList()
    linkedlst.printListFromEnd(linkedlst.head)
    linkedlst.isLinkedListLengthEven()
