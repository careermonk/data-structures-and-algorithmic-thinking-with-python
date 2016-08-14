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
            self.set_data(data)
            self.set_next(next)
        # method for setting the data field of the node    
        def set_data(self, data):
            self.data = data
        # method for getting the data field of the node   
        def get_data(self):
            return self.data
          # method for setting the next field of the node
        def set_next(self, next):
            self.next = next
           # method for getting the next field of the node    
        def get_next(self):
            return self.next
        # returns true if the node points to another node
        def has_next(self):
                return self.next != None
    answer = []

    # initialize circular linked list
    head = Node(0)
    prev = head
    for n in range(1, n):
        currentNode = Node(n)
        prev.set_next(currentNode)
        prev = currentNode
    prev.set_next(head)  # set the last node to point to the front (circular list)

    # extract items from linked list in proper order
    currentNode = head
    counter = 0
    while currentNode.get_next() != currentNode:
        counter += 1
        if counter == m:
            counter = 0
            prev.set_next(currentNode.next)
            answer.append(currentNode.get_data())
        else:
            prev = currentNode
        currentNode = currentNode.get_next()
    
    answer.append(currentNode.get_data())
    return answer
        

print str(getJosephusPosition(6, 3))
