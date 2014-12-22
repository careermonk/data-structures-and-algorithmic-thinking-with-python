# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def sortedArrayToBST(root, array):
	length = len(array)
	if length == 0: 
		return None
	if length == 1: 
		return TreeNode(array[0])
	root = BSTNode(array[length / 2])
	root.left = sortedArrayToBST(array[:length / 2])
	root.right = sortedArrayToBST(array[length / 2 + 1:])
	return root
