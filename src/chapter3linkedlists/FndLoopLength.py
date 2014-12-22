# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

'''Complexity
Space : O(n) Time: O(1)'''
 
 
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
         
    def isEmpty(self):
        return self.head == None
     
    def insertAtBeg(self, item):
        node = Node(item)
        node.setNext(self.head)
        self.head = node
         
    def length(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
     
    def search(self, item):
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                 
        return found
     
    def insertAtEnd(self, item):
        current = self.head
         
        while current.getNext() != None:
            current = current.getNext()
             
        node = Node(item)
        current.setNext(node)
         
    def insertBeforeItem(self, inItem, item):
        current = self.head
        previous = None
        found = False
        stop = False
         
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
                stop = True
            else:
                previous = current
                current = current.getNext()
                 
        node = Node(inItem)
        previous.setNext(node)
        node.setNext(current)
         
         
    def insertAfterItem(self, inItem, item):
        current = self.head
         
        found = False
        stop = False
         
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
                stop = True
            else:
#                previous = current
                current = current.getNext()
        successor = current.getNext()       
        node = Node(inItem)
        current.setNext(node)
        node.setNext(successor)
         
             
         
         
         
    def printList(self):
        current = self.head
         
        while current != None:
            print current.getData()
            current = current.getNext()
             
             
    def remove(self, item):
        found = False
        current = self.head
        previous = None
         
        while current.getNext() != None and not found:
            if current.getData() == item:
                print current.getData()
                print previous.getData()
                found = True
                previous.setNext(current.next)
            else:
                previous = current
                current = current.getNext()
                 
    def induceCycle(self, end, start):
        current = self.head
        stop = False
        endnodeFound = False
        endnodePointer = None
        count = 0
        while current != None and not stop:
            count += 1
            if count == end:
                endnodeFound = True
                endnodePointer = current.getNext()
                 
            else:
                if count == start:
                    stop = True
                else:
                    current = current.getNext()
                     
        current.setNext(endnodePointer)
         
    def detectCycle(self):
        hare = self.head
        tortoise = self.head
         
        while (hare and tortoise):
            hare = hare.getNext()
            if (hare == tortoise):
                return True
             
            if hare == None:
                return False
             
            hare = hare.getNext()
            if (hare == tortoise):
                return True
             
            tortoise = tortoise.getNext()
    
	def detectCycleStart(self) :
	    if None == self.head or None == self.head.next:
	      return None
	 
	    # slow and fast both started at head after one step,
	    # slow is at self.head.next and fast is at self.head.next.next
	    slow = self.head.next
	    fast = slow.next
	    # each keep walking until they meet again.
	    while slow != fast:
	      slow = slow.next
	      try:
		fast = fast.next.next
	      except AttributeError:
		return None  # no cycle if NoneType reached
	 
	    # from self.head to beginning of loop is same as from fast to
	    # beginning of loop
	    slow = self.head
	    while slow != fast:
	      slow = slow.next
	      fast = fast.next
	 
	    return slow  # beginning of loop
    
	def fndLoopLength(self) :
	    if None == self.head or None == self.head.next:
	      return 0
	 
	    # slow and fast both started at head after one step,
	    # slow is at self.head.next and fast is at self.head.next.next
	    slow = self.head.next
	    fast = slow.next
	    # each keep walking until they meet again.
	    while slow != fast:
	      slow = slow.next
	      try:
	        fast = fast.next.next
	      except AttributeError:
	        return 0  # no cycle if NoneType reached
	 
	    loopLength = 0	
	    slow = slow.next
	    while slow != fast:
	      slow = slow.next
	      loopLength = loopLength + 1    
	    
	    return loopLength          
         
         
if __name__ == "__main__":
    linkedlst = LinkedList()
    linkedlst.insertAtBeg(1)
    linkedlst.insertAtBeg(2)
    linkedlst.insertAtEnd(3)
    linkedlst.insertBeforeItem(4, 3)
    linkedlst.insertAfterItem(5, 1)
    linkedlst.insertAtEnd(6)
    linkedlst.insertAtEnd(8)
    linkedlst.insertAtEnd(7)
     
     
    linkedlst.printList()
     
    linkedlst.induceCycle(2, 8)
    print linkedlst.detectCycle()
    print linkedlst.fndLoopLength()
    print linkedlst.detectCycleStart()
