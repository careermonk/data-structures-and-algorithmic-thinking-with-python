# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def getJosephusPosition(n, m):
    class Node:
        def __init__(self, data=None, next=None):
            self.setData(data)
            self.setNext(next)
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
    answer = []

    # initialize circular linked list
    head = Node(0)
    prev = head
    for n in range(1, n):
        currentNode = Node(n)
        prev.setNext(currentNode)
        prev = currentNode
    prev.setNext(head)  # set the last node to point to the front (circular list)

    # extract items from linked list in proper order
    currentNode = head
    counter = 0
    while currentNode.getNext() != currentNode:
        counter += 1
        if counter == m:
            counter = 0
            prev.setNext(currentNode.next)
            answer.append(currentNode.getData())
        else:
            prev = currentNode
        currentNode = currentNode.getNext()
    
    answer.append(currentNode.getData())
    return answer
        

print str(getJosephusPosition(6, 3))
