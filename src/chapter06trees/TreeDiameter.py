# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def findMaxLen(root):
	nMaxLen = 0
	if (root == None):
		return 0
	if (root.left == None):
		root.nMaxLeft = 0
	if (root.right == None):
		root.nMaxRight = 0
	if (root.left != None):
		findMaxLen(root.left)
	if (root.right != None):
		findMaxLen(root.right)
	if (root.left != None):
		nTempMaxLen = 0
		nTempMaxLen = max(root.left.nMaxLeft, root.left.nMaxRight)
		root.nMaxLeft = nTempMaxLen + 1

	if (root.right != None):
		nTempMaxLen = 0
		nTempMaxLen = max(root.right.nMaxLeft, root.right.nMaxRight)
		root.nMaxRight = nTempMaxLen + 1
	
	if (root.nMaxLeft + root.nMaxRight > nMaxLen):
		nMaxLen = root.nMaxLeft + root.nMaxRight
	return nMaxLen

ptr = 0
def diameterOfTree(root):
	global ptr
	if(not root) :
		return 0
	left = diameterOfTree(root.left);
	right = diameterOfTree(root.right);

	if(left + right > ptr):
	      ptr = left + right
	return max(left, right) + 1
 

# Alternative Coding
def diameter(root):
	if (root == None): 
		return 0

	lHeight = height(root.eft)
	rHeight = height(root.right)
	lDiameter = diameter(root.left)
	rDiameter = diameter(root.right)
	return max(lHeight + rHeight + 1, max(lDiameter, rDiameter))

# The function Compute the "height" of a tree. Height is the number f nodes along 
# the longest path from the root node down to the farthest leaf node.
def height(root):
	if (root == None) :
		return 0
	return 1 + max(height(root.left), height(root.right))
