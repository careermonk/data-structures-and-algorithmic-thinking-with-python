# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

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
	    

# Post-order recursive traversal. The nodes' values are appended to the result list in traversal order
def postorderRecursive(root):
	if not root:
		return

	postorderRecursive(root.left)
	postorderRecursive(root.right)
	print root.data
    
# Pre-order recursive traversal. The nodes' values are appended to the result list in traversal order
def preorderRecursive(root):
    if not root:
        return
    
    print root.data
    preorderRecursive(root.left)
    preorderRecursive(root.right)

i = 0      
def buildTreeFromPreOrder(A):
	global i
     	if(A == None or i >= len(A)):  # Boundary Condition
		return None
	newNode = BinaryTree(A[i])
	newNode.data = A[i]
	newNode.left = newNode.right = None


	if(A[i] == "L"):  # On reaching leaf node, return
		return newNode

	i += 1  # Populate left sub tree
	newNode.left = buildTreeFromPreOrder(A)

	i += 1  # Populate right sub tree
	newNode.right = buildTreeFromPreOrder(A)

	return newNode

root = buildTreeFromPreOrder(["I", "I", "L", "I", "L", "L", "I", "L", "L"])
postorderRecursive(root)


	
