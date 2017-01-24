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
    # Constructor to initialize data
    # If data is not given by user,its taken as None 
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
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
    # method for setting the next field of the node
    def setPrev(self, prev):
        self.prev = prev
       # method for getting the next field of the node    
    def getPrev(self):
        return self.prev
    # returns true if the node points to another node
    def hasPrev(self):
            return self.prev != None	    
    # __str__ returns string equivalent of Object
    def __str__(self):
        return "Node[Data = %s]" % (self.data,)

class DoubleLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        if (self.head == None):  # To imply that if head == None
            self.head = Node(data)
            self.tail = self.head
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = Node(data, None, current)
            self.tail = current.next

    def delete(self, data):
        current = self.head
        # If given item is the first element of the linked list
        if current.data == data:
            self.head = current.next
            self.head.prev = None
            return True
        
        # In case the linked list is empty
        if current == None:
            return False

        # If the element is at the last
        if self.tail == data:
            self.tail = self.tail.prev
            self.tail.next = None
            return True

        # If the element is absent or in the middle of the linked list
        while current != None:
            if current.data == data :
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
            current = current.next
     
        # The element is absent
        return False
	
    def insertAtBeginning(self, data):
        newNode = Node(data, None, None)
        if (self.head == None):  # To imply that if head == None
            self.head = self.tail = newNode
        else:
            newNode.setPrev(None)
            newNode.set_next(self.head)
            self.head.setPrev(newNode)
            self.head = newNode


    def getNode(self, index):
        currentNode = self.head
        if currentNode == None:
            return None
        i = 0
        while i < index and currentNode.get_next() is not None:
            currentNode = currentNode.get_next()
            if currentNode == None:
                break
            i += 1
        return currentNode
		
    def insertAtGivenPosition(self, index, data):
        newNode = Node(data)
        if self.head == None or index == 0:
            self.insertAtBeginning(data)
        elif index > 0:
            temp = self.getNode(index) 
            if temp == None or temp.get_next() == None:	
                self.insert(data)
            else:
                newNode.set_next(temp.get_next())
                newNode.setPrev(temp)
                temp.get_next().setPrev(newNode)
                temp.set_next(newNode)
		
    def find(self, data):
        current = self.head
        while current != None:
            if current.data == data :
                return True
            current = current.next
        return False

    def fwd_print(self):
        current = self.head
        if current == None:
            print("No elements")
            return False
        while (current != None):
            print (current.data) 
            current = current.next
        return True

    def rev_print(self):
        current = self.tail
        if (self.tail == None):
            print("No elements")
            return False

        while (current != None):
            print (current.data)
            current = current.prev
        return True

if __name__ == '__main__':
    # Initializing list
    l = DoubleLinkedList()

    # Inserting Values
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)

    # Forward Print
    l.fwd_print()

    # Reverse Print
    l.rev_print()

    # Try to find 3 in the list
    if (l.find(3)):
        print("Found")
    else :
        print("Not found")

    # Delete 3 from the list
    l.delete(3)

    # Forward Print
    l.fwd_print()

    # Reverse Print
    l.rev_print()

    # Now if we find 3, we will not get it in the list
    if (l.find(3)):
        print("Found")
    else :
        print("Not found")
