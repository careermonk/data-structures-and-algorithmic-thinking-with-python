# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

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
	global prev
	if(not root): 
		return None

	if(not FloorInBSTUtil(root.left, data)):
		return 0
	if(root.data == data) :
		return root

	if(root.data > data): 	
		return prev

	prev = root
	return FloorInBSTUtil(root.right, data)

def CeilInBST(root, data):
	# Base case
	if(root == None):
		return -sys.maxint
	# We found equal data
	if(root.data == data):
		return root.data

	# If root's data is smaller, ceil must be in right subtree
	if(root.data < data):
		return CeilInBST(root.right, data)
	# Else, either left subtree or root has the ceil data
	ceil = CeilInBST(root.left, data)
	if ceil >= data:
		return ceil
	else: return root.data
	
root = BSTNode(3)
insertNode(root, BSTNode(57))
insertNode(root, BSTNode(14))
insertNode(root, BSTNode(35))
insertNode(root, BSTNode(2))
insertNode(root, BSTNode(98))
# inOrderTraversal(root)
for i  in range(10):
	print i, "ceil is ", CeilInBST(root, i)
