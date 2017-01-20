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
def inorderIterative(root, result):
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
            result.append(node.data)
            node = node.right

# Post-order iterative traversal. The nodes' values are appended to the result list in traversal order
def postorderTraversal(root, result):
    result = []
    visited = set()
    stack = []
    if root != None:
        stack.append(root)
    while len(stack)>0:
        node = stack.pop()
        if node in used:
            result.append(node.val)
        else:
            visited.add(node)
            stack.append(node)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)

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
