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
	# method for setting the last field of the node
	def setLast(self, last):
		self.last = last
	# method for getting the last field of the node    
	def getLast(self):
		return self.last	
	# returns true if the node points to another node
	def hasNext(self):
		return self.next != None

    
class Stack(object):
    def __init__(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node()
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.getData()
        self.head = self.head.getNext()
        return temp
	
    def peek(self):
        if self.head is None:
            raise IndexError
        return self.head.getData()

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
		return self.rear.getData()

	def queueFront(self):
		if self.front is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.front.getData()

	def deQueue(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		result = self.rear.getData()
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
	def setData(self, data):
		self.data = data
	# get data   
	def getData(self):
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

def insertInBinaryTreeUsingLevelOrder(root, data):
	newNode = BinaryTree(data)
	if root is None:
		root = newNode
		return root

	q = Queue()
	q.enQueue(root)
	node = None
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO

		if data == node.getData():
			return root
		if node.left is not None:
			q.enQueue(node.left)
		else:
			node.left = newNode
			return root	
		if node.right is not None:
			q.enQueue(node.right)
		else:
			node.right = newNode
			return root

def findLevelwithMaxSum(root):
	if root is None:
		return 0
	q = Queue()
	q.enQueue(root)
	q.enQueue(None)
	node = None
	level = maxLevel = currentSum = maxSum = 0 
	while not q.isEmpty():
		node = q.deQueue()  # dequeue FIFO
		# If the current level is completed then compare sums
		if(node == None): 
			if(currentSum > maxSum):
				maxSum = currentSum
				maxLevel = level

			currentSum = 0
			# place the indicator for end of next level at the end of queue
			if not q.isEmpty():  
				q.enQueue(None)
				level += 1		
		else:
			currentSum += node.getData()
			if node.left is not None:
				q.enQueue(node.left)

			if node.right is not None:
				q.enQueue(node.right)
	return maxLevel
	
		
# In-order recursive traversal. The nodes' values are appended to the result list in traversal order
def inorderRecursive(root):
	if not root:
		return

	inorderRecursive(root.left)
	print root.data
	inorderRecursive(root.right)

def deleteBinaryTree(root):
	if(root == None) :
	       return
	deleteBinaryTree(root.left);
	deleteBinaryTree(root.right);
	del root



root = BinaryTree(11)
root = insertInBinaryTreeUsingLevelOrder(root, 1)
root = insertInBinaryTreeUsingLevelOrder(root, 2)
root = insertInBinaryTreeUsingLevelOrder(root, 3)
root = insertInBinaryTreeUsingLevelOrder(root, 4)
root = insertInBinaryTreeUsingLevelOrder(root, 125)
root = insertInBinaryTreeUsingLevelOrder(root, 225)
# inorderRecursive(root)
print findLevelwithMaxSum(root)
