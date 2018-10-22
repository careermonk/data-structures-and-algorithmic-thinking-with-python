# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Node of a Singly Linked List
class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None
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

# class for defining a linked list   
class LinkedList(object):
     
    # initializing a list
    def __init__(self):
        self.length = 0
        self.head = None
         
    # method to add a node in the linked list
    def addNode(self, node):
        if self.length == 0:
            self.addBeg(node)
        else:
            self.addLast(node)
             
         
    # method to add a node at the beginning of the list with a data   
    def addBeg(self, node):
        newNode = node
        newNode.next = self.head
        self.head = newNode
        self.length += 1
         
    # method to add a node after the node having the data=data. The data of the new node is value2
    def addAfterValue(self, data, node):
        newNode = node
        currentnode = self.head
         
        while currentnode.next != None or currentnode.data != data:
            if currentnode.data == data:
                newNode.next = currentnode.next
                currentnode.next = newNode
                self.length = self.length + 1
                return
            else:
                currentnode = currentnode.next
                 
        print "The data provided is not present"
                 
    # method to add a node at a particular position
    def addAtPos(self, pos, node):
        count = 0
        currentnode = self.head
        previousnode = self.head
         
        if pos > self.length or pos < 0:
            print "The position does not exist. Please enter a valid position"
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = node
                    node.next = currentnode
                    self.length += 1
                    return
                     
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next
         
         
                 
    # method to add a node at the end of a list
    def addLast(self, node):
        currentnode = self.head
         
        while currentnode.next != None:
            currentnode = currentnode.next
 
        newNode = node
        newNode.next = None
        currentnode.next = newNode
        self.length = self.length + 1
     
     
    # method to delete the first node of the linked list
    def deleteBeg(self):
        if self.length == 0:
            print "The list is empty"
        else:
            self.head = self.head.next
            self.length -= 1
     
    # method to delete the last node of the linked list
    def deleteLast(self):
         
        if self.length == 0:
            print "The list is empty"
        else:
            currentnode = self.head
            previousnode = self.head
             
            while currentnode.next != None:
                previousnode = currentnode
                currentnode = currentnode.next
                 
            previousnode.next = None
             
            self.length -= 1
             
         
    # method to delete a node after the node having the given data
    def deleteValue(self, data):
        currentnode = self.head
        previousnode = self.head
         
        while currentnode.next != None or currentnode.data != data:
            if currentnode.data == data:
                previousnode.next = currentnode.next
                self.length -= 1
                return
                    
            else:
                previousnode = currentnode
                currentnode = currentnode.next
                 
        print "The data provided is not present"
                 
         
         
    # method to delete a node at a particular position
    def deleteAtPos(self, pos):
        count = 0
        currentnode = self.head
        previousnode = self.head
 
        if pos > self.length or pos < 0:
            print "The position does not exist. Please enter a valid position"
        # to deletle the first position of the linkedlist
        elif pos == 1:
            self.delete_beg()
            self.length -= 1
        else:        
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next
                     
             
 
     
    # returns the length of the list        
    def getLength(self):
        return self.length
     
    # returns the first element of the list
    def getFirst(self):
        if self.length == 0:
            print "The list is empty"
        else:
            return self.head.data
     
    # returns the last element of the list
    def getLast(self):
         
        if self.length == 0:
            print "The list is empty"
        else:
            currentnode = self.head
             
            while currentnode.next != None:
                currentnode = currentnode.next
                 
            return currentnode.data
     
    # returns node at any position
    def getAtPos(self, pos):
        count = 0
        currentnode = self.head
         
        if pos > self.length or pos < 0:
            print "The position does not exist. Please enter a valid position"
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    return currentnode.data
                else:
                    currentnode = currentnode.next
 
                     
    # method to print the whole list
    def print_list(self):
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.next 
             
        print nodeList  

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
ll = LinkedList()
ll.addNode(node1)
ll.addNode(node2)
ll.addNode(node3)
ll.addNode(node4)
ll.addNode(node5)
ll.print_list()
