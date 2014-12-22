# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

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

root = BSTNode(3)
insertNode(root, BSTNode(7))
insertNode(root, BSTNode(1))
insertNode(root, BSTNode(5))
insertNode(root, BSTNode(2))
insertNode(root, BSTNode(9))
inOrderTraversal(root)
