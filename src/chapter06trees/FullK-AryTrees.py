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
		
'''Binary Tree Class and its methods'''
class BinaryTree:
	def __init__(self, data):
		self.data = data  # root node
		self.left = None  # left child
		self.right = None  # right child
	# set data
	def set_data(self, data):
		self.data = data
	# get data   
	def get_data(self):
		return self.data	
	# get left child of a node
	def getLeft(self):
		return self.left
	# get right child of a node
	def getRight(self):
		return self.right
	
	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.left = self.left
			self.left = temp

	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.right = self.right
			self.right = temp

def levelOrder (root):
	Q = Queue()
	if(root == None): 
		return None

	Q.enQueue(root)
	while(not Q.isEmpty()):
		temp = Q.deQueue()
		print temp.data
		if(temp.left):
			Q.enQueue(temp.left)
		if(temp.right): 
			Q.enQueue(temp.right)

class KaryTreeNode:
    def __init__ (self, k, data=None):
        self.data = data
        self.childList = []

def BuildKaryTree(A, k):
	n = len(A)
	if n <= 0:
		return None
	index = 0		
	root = KaryTreeNode(None, A[0])
	if(not root):
		print("Memory Error")
		return
	Q = Queue()
	if(Q == None): 
		return None
	Q.enQueue(root)
	while(not Q.isEmpty()):
		temp = Q.deQueue()
		for i in range(0, k):
			index += 1
			if index < n:
				temp.childList.insert(i, KaryTreeNode(None, A[index]))
				Q.enQueue(temp.childList[i])
	return root
	
def preorderRecursive(kroot):
	if not kroot:
		return
	print kroot.data	
	for node in kroot.childList:
		preorderRecursive(node)		
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
kroot = BuildKaryTree(A, 3)	
preorderRecursive(kroot)
