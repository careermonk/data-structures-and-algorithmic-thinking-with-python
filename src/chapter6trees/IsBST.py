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

def IsBST(root):
	if root == None:
                  return 1
	# false if left is > than root 
	if root.getLeft() != None and root.getLeft().getData() > root.getData():
                  return 0

	# false if right is < than root 
	if root.getRight() != None and root.getRight().getData() < root.getData():
                  return 0

	# false if, recursively, the left or right is not a BST 
	if not IsBST(root.getLeft()) or not IsBST(root.getRight()):
                  return 0

	# passing all that, it's a BST 
	return 1

def IsBST2(root, min, max):
	if root == None:
	    return 1
	if root.getData() <= min or root.getData() >= max:
	    return 0
	result = IsBST2(root.getLeft(), min, root.getData())
	result = result and IsBST2(root.getRight(), root.getData(), max)
	return result

# Returns true if a binary tree is a binary search tree 
def IsBST3(root):
	if root == None:
                  return 1

	# false if the max of the left is > than root 
	if(root.getLeft() != None and FindMax(root.getLeft()) > root.getData())
                  return 0

	# false if the min of the right is <= than root 
	if(root.getRight() != None and FindMin(root.getRight()) < root.getData())
                  return 0

	# false if, recursively, the left or right is not a BST 
	if(not IsBST3(root.getLeft()) or not IsBST3(root.getRight())) 
                  return 0

	# passing all that, it's a BST 
	return 1
	
def isBST4(root, previousValue=[NEG_INFINITY]): 
	if root is None: 
		return 1   
	if not isBST4(root.getLeft(), previousValue): 
		return False   
	if root.getData() < lastNode[0]: 
		return 0   
	previousValue = root.getData()   
	return isBST4(root.getRight(), previousValue)
