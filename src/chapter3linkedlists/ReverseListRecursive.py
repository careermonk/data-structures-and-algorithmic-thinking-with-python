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
         
    def setData(self, data):
        self.data = data
     
    def getData(self):
        return self.data
     
    def setNext(self, next):
        self.next = next
         
    def getNext(self):
        return self.next
     
     
class LinkedList:
    def __init__(self):
        self.head = None
    
    def recursiveReverseList(self) :
		self.reverseRecursive(self.head)
		
    def reverseRecursive(self, n) :
	if None != n:
		right = n.getNext()
		if self.head != n:
			n.setNext(self.head)
			self.head = n
		else:
			n.setNext(None)
		self.reverseRecursive(right)

    def insertAtEnd(self, item):
        current = self.head
        if  current == None:
            node = Node(item)
            node.setNext(None)
            self.head = node
            return
            
        while current.getNext() != None:
            current = current.getNext()
             
        node = Node(item)
        current.setNext(node)
         
    def printList(self):
        current = self.head
         
        while current != None:
            print current.getData()
            current = current.getNext()
             
	

if __name__ == "__main__":
    linkedlst = LinkedList()
    linkedlst.insertAtEnd(1)
    linkedlst.insertAtEnd(2)
    linkedlst.insertAtEnd(3)
    linkedlst.insertAtEnd(4)
     
    linkedlst.printList()
    linkedlst.recursiveReverseList()
    linkedlst.printList()
