# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

'''Generic Tree Class and its methods'''
class GenericTreeNode:
	def __init__(self, data):
		self.data = data  # root node
		self.firstChild = None  # left child
		self.nextSibling = None  # right child
	# set data
	def set_data(self, data):
		self.data = data
	# get data   
	def get_data(self):
		return self.data	
	# get firstChild child of a node
	def getFirstChild(self):
		return self.firstChild
	# get nextSibling child of a node
	def getNextSibling(self):
		return self.nextSibling
	# get firstChild child of a node
	def setFirstChild(self, firstChild):
		self.firstChild = firstChild
	# get nextSibling child of a node
	def setNextSibling(self, nextSibling):
		self.nextSibling = nextSibling
	def insertLeft(self, newNode):
		if self.firstChild == None:
			self.firstChild = GenericTreeNode(newNode)
		else:
			temp = GenericTreeNode(newNode)
			temp.firstChild = self.firstChild
			self.firstChild = temp

	def insertRight(self, newNode):
		if self.nextSibling == None:
			self.nextSibling = GenericTreeNode(newNode)
		else:
			temp = GenericTreeNode(newNode)
			temp.nextSibling = self.nextSibling
			self.nextSibling = temp
	    
# Pre-order recursive traversal. The nodes' values are appended to the result list in traversal order
def preorderRecursive(root, result):
    if not root:
        return
    
    result.append(root.data)
    preorderRecursive(root.firstChild, result)
    preorderRecursive(root.nextSibling, result)

# In-order recursive traversal. The nodes' values are appended to the result list in traversal order
def inorderRecursive(root, result):
	if not root:
		return

	inorderRecursive(root.firstChild, result)
	result.append(root.data)
	inorderRecursive(root.nextSibling, result)

# Post-order recursive traversal. The nodes' values are appended to the result list in traversal order
def postorderRecursive(root, result):
    if not root:
        return
    
    postorderRecursive(root.firstChild, result)
    postorderRecursive(root.nextSibling, result)
    result.append(root.data)

# Pre-order iterative traversal. The nodes' values are appended to the result list in traversal order
def preorderIterative(root, result):
    if not root:
        return

    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.nextSibling: stack.append(node.nextSibling)
        if node.firstChild: stack.append(node.firstChild)    

# In-order iterative traversal. The nodes' values are appended to the result list in traversal order
def inorderIterative(root, result):
	if not root:
		return

	stack = []
	node = root
	while stack or node:
		if node:
			stack.append(node)
			node = node.firstChild
		else:
			node = stack.pop()
			result.append(node.data)
			node = node.nextSibling

# Post-order iterative traversal. The nodes' values are appended to the result list in traversal order
def postorderIterative(root, result):
    if not root:
        return

    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.firstChild
        else:
            node = stack.pop()
            if node.nextSibling and not node.nextSibling in visited:
                stack.append(node)
                node = node.nextSibling
            else:
                visited.add(node)
                result.append(node.data)
                node = None

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

def levelOrder(root, result):
    if root is None:
      return
 
    q = Queue()
    q.enQueue(root)
    n = None
 
    while not q.isEmpty():
      n = q.deQueue()  # dequeue FIFO
      result.append(n.get_data())
      if n.firstChild is not None:
        q.enQueue(n.firstChild)
 
      if n.nextSibling is not None:
        q.enQueue(n.nextSibling)	


def siblingsCount(current):
	count = 0
	while(current):
	       count += 1
	       current = current.nextSibling
	return count

root = GenericTreeNode(11)
print(root.get_data())

root.insertLeft(1)
root.insertLeft(10)
root.insertLeft(1100)
root.insertRight(5)
root.getNextSibling().set_data(2)
result = []
levelOrder(root, result)
print result
print siblingsCount(root)

