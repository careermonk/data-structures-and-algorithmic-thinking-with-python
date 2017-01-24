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

class BSTNode(object):
    '''
    A binary search tree (BST) node
    '''
    def __init__(self, data, data2):
        self.data = data
	self.data2 = data2	
        self.left = None
        self.right = None
	
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
    # get left child of a node
    def setLeft(self, left):
        self.left = left
    # get right child of a node
    def setRight(self, right):
        self.right = right
	
    def search(self, data):
        if self.data == data:
            return self

        if self.left is not None and self.data > data:
            return self.left.search(data)
        elif self.right is not None:
            return self.right.search(data)

        return None
    
    def insert(self, data, data2):
        self.insertNode(BSTNode(data, data2))

    def insertNode(self, node):
        '''
        Inserts a data to the tree with self as root
        
        @param data The data to be inserted
        '''
        # Base case: empty root node
        if self.data is None:
            self.data = node.data
	    self.data2 = node.data2
            return

        if node.data < self.data:
            if not self.left:
                self.left = node
            else:
                self.left.insertNode(node)
        elif node.data > self.data:
            if not self.right:
                self.right = node
            else:
                self.right.insertNode(node)
        else:
            pass  # Duplicate values are ignored

    def delete(self, data):
        # Base case: root node
        if self.data == data:
            self.deleteNode()
        elif data < self.data and self.left is not None:
            self.left.delete(data)
        elif self.right is not None:
            self.right.delete(data)

    def deleteNode(self):
        '''
        Removes the node from its tree, updating its children node pointers, if any.
        @param parent the node's parent
        '''
        if self.right and self.left:
            # Node has two children Replace data with successor s and delete s
            if self.right:
                s = self.successor()
                self.data = s.data
                s.deleteNode()
        elif self.right or self.left:
            # Node has single child. Replace it with only child
            child = self.right is not None and self.right or self.left

            self.data = child.data
            self.left = child.left
            self.right = child.right
        else:
            # None has no children, erase data and update parent
            self.data = None

    def successor(self):
        s = None

        if self.right:
            s = self.right
            while s.left:
                s = s.left

        return s

    def predecessor(self):
        s = None

        if self.left:
            s = self.left
            while s.right:
                s = s.right

        return s

    def __str__(self):
        return "(%s, l: %s, r: %s)" % (self.data, self.left is not None and self.left.data or 'N', self.right is not None and self.right.data or 'N')

def inorderRecursive(root):
	if not root:
		return
	inorderRecursive(root.left)
	print root.data, "--->", root.data2 
	inorderRecursive(root.getRight())

def findMin(root):
	currentNode = root
	if currentNode == None:  
		return None
	while currentNode.getLeft() != None:
		currentNode = currentNode.getLeft()
	return currentNode

# Search the key from node, iteratively
def findMax(root):
	currentNode = root
	if currentNode == None:  
		return None
	while currentNode.right != None:
		currentNode = currentNode.right
	return currentNode

def treeCompression (root):
	Q = Queue()
	if(root == None): 
		return None

	Q.enQueue(root)
	while(not Q.isEmpty()):
		temp = Q.deQueue()
		if(temp.left and temp.right and (temp.left.data2 > temp.right.data2)):
			temp2 = findMax(temp.left)
		else: temp2 = findMin(temp.right)

		temp.data2 = temp2.data2  # Process current node
		root.delete(temp.data)
		if(temp.left):
			Q.enQueue(temp.left)
		if(temp.right): 
			Q.enQueue(temp.right)
			
root = BSTNode(6, 5)
root.insert(4, 2)
root.insert(9, 2)
root.insert(2, 0)
root.insert(5, 0)
root.insert(7, 1)
root.insert(8, 0)
inorderRecursive(root)
print treeCompression(root)
inorderRecursive(root)
inorderRecursive(root)
