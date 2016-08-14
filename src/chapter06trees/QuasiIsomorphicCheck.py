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
	# get left child of a node
	def setLeft(self, left):
		self.left = left
	# get right child of a node
	def setRight(self, right):
		self.right = right
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
	    
# Pre-order recursive traversal. The nodes' values are appended to the result list in traversal order
def preorderRecursive(root, result):
    if not root:
        return
    
    result.append(root.data)
    preorderRecursive(root.left, result)
    preorderRecursive(root.right, result)

# In-order recursive traversal. The nodes' values are appended to the result list in traversal order
def inorderRecursive(root, result):
	if not root:
		return

	inorderRecursive(root.left, result)
	result.append(root.data)
	inorderRecursive(root.right, result)

# Post-order recursive traversal. The nodes' values are appended to the result list in traversal order
def postorderRecursive(root, result):
    if not root:
        return
    
    postorderRecursive(root.left, result)
    postorderRecursive(root.right, result)
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
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)    

# In-order iterative traversal. The nodes' values are appended to the result list in traversal order
def inorderIterative(root):
	if not root:
		return

	stack = []
	node = root
	while stack or node:
		if node:
			stack.append(node)
			node = node.left
		else:
			node = stack.pop()
			print node.data
			node = node.right

# Post-order iterative traversal. The nodes' values are appended to the result list in traversal order
def postorderIterative(root):
    if not root:
        return

    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                print node.data
                node = None

def quasiIsomorphic(root1, root2):
	if(not root1 and not root2): 
		return 1
	if((not root1 and root2) or (root1 and not root2)):
	        return 0
	return (quasiIsomorphic(root1.left, root2.left) and quasiIsomorphic(root1.right, root2.right)
	         or quasiIsomorphic(root1.right, root2.left) and quasiIsomorphic(root1.left, root2.right))
	

root1 = BinaryTree(11)
root1.insertLeft(1)
root1.insertLeft(10)
root1.insertLeft(1100)
root1.insertRight(5)
root1.getRight().set_data(2)
postorderIterative(root1)

root2 = BinaryTree(99)
root2.insertLeft(9)
root2.insertLeft(910)
root2.insertLeft(9900)
root2.insertRight(8)
root2.getRight().set_data(2)
postorderIterative(root2)
print "QuasiIsomorphic:", quasiIsomorphic(root1, root2)
