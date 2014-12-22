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
	
    def sqrtNodes(self):
	sqrtNode = None
	currentNode = self.head
	i = j = 1
	while currentNode != None:
		if i == j * j:
			if sqrtNode == None:
				sqrtNode = self.head
			else:
				sqrtNode = sqrtNode.getNext()
			j = j + 1
		i = i + 1
		currentNode = currentNode.getNext()
		
	print (sqrtNode.getData())
			
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

if __name__ == "__main__":
    linkedlst = LinkedList()
    linkedlst.insertAtEnd(1)
    linkedlst.insertAtEnd(2)
    linkedlst.insertAtEnd(3)
    linkedlst.insertAtEnd(4)
    linkedlst.insertAtEnd(5)
    linkedlst.insertAtEnd(11)
    linkedlst.insertAtEnd(12)
    linkedlst.insertAtEnd(13)
    linkedlst.insertAtEnd(14)
    linkedlst.insertAtEnd(15)
    
    linkedlst.sqrtNodes()
