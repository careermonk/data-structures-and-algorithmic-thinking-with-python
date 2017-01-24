# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Node of a Singly Linked List
class Node:
	# constructor
	def __init__(self, data=None, next=None):
		self.data = data
		self.last = None
		self.next = next
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
	# method for setting the last field of the node
	def setLast(self, last):
		self.last = last
	# method for getting the last field of the node    
	def getLast(self):
		return self.last	
	# returns true if the node points to another node
	def has_next(self):
		return self.next != None

    
class Stack(object):
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node()
        temp.set_data(data)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.get_data()
        self.head = self.head.get_next()
        return temp
	
    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.get_data()

    def isEmpty(self):
        return self.head == None
	
class Queue(object):
	def __init__(self, data=None):
		self.front = None
		self.rear = None
		self.size = 0

	def enQueue(self, data):
		self.lastNode = self.front
		self.front = Node(data, self.front)
		if self.lastNode:
			self.lastNode.setLast(self.front)
		if self.rear is None:
			self.rear = self.front
		self.size += 1

	def queueRear(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.rear.get_data()

	def queueFront(self):
		if self.front is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.front.get_data()

	def deQueue(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		result = self.rear.get_data()
		self.rear = self.rear.last
		self.size -= 1
		return result

	def size(self):
		return self.size
		
	def isEmpty(self):
		return self.size == 0
import sys
class BSTNode:
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data

def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)

def deleteNode(root, data):
	""" delete the node with the given data and return the root node of the tree """	    
	if root.data == data:
		# found the node we need to delete
		if root.right and root.left: 
			# get the successor node and its parent 
			[psucc, succ] = findMin(root.right, root)
			# splice out the successor
			# (we need the parent to do this) 
			if psucc.left == succ:
				psucc.left = succ.right
			else:
				psucc.right = succ.right					
			# reset the left and right children of the successor
			succ.left = root.left
			succ.right = root.right
			return succ                
		else:
			# "easier" case
			if root.left:
				return root.left  # promote the left subtree
			else:
				return root.right  # promote the right subtree 
	else:
		if root.data > data:  # data should be in the left subtree
			if root.left:
				root.left = deleteNode(root.left, data)
			# else the data is not in the tree 
		else:  # data should be in the right subtree
			if root.right:
				root.right = deleteNode(root.right, data)
	return root

def findMin(root, parent):
	""" return the minimum node in the current tree and its parent """
	# we use an ugly trick: the parent node is passed in as an argument
	# so that eventually when the leftmost child is reached, the 
	# call can return both the parent to the successor and the successor
	if root.left:
		return findMin(root.left, root)
	else:
		return [parent, root]

def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print root.data
    inOrderTraversal(root.right)

def preOrderTraversal(root):
    if not root:
        return        
    print root.data
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)    

prev = None
def FloorInBST(root, data):
	global prev
	return FloorInBSTUtil(root, data)

def FloorInBSTUtil(root, data):
	if(not root): 
		return sys.maxint

	if(root.data == data) :
		return root.data

	if(data < root.data): 	
		return FloorInBSTUtil(root.left, data)

	floor = FloorInBSTUtil(root.right, data)
	if floor <= data:
		return floor
	else: return root.data 

import sys
import math
def ClosestInBST(root, data):
	if(root == None):
		return root
	if(root.data == data):
		return root
	if(data < root.data):
		if(not root.left):
			return root
		temp = ClosestInBST(root.left, data)
		if (abs(temp.data - data) > abs(root.data - data)):
			return root 
		else: return temp
	else:
		if(not root.right):
			return root
		temp = ClosestInBST(root.right, data)
		if (abs(temp.data - data) > abs(root.data - data)):
			return root 
		else: return temp		
	return None




root = BSTNode(3)
insertNode(root, BSTNode(17))
insertNode(root, BSTNode(11))
insertNode(root, BSTNode(55))
insertNode(root, BSTNode(23))
insertNode(root, BSTNode(99))
print ClosestInBST(root, 70).data
