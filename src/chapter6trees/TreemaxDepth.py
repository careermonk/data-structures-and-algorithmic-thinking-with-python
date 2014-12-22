# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def maxDepth(root):
	if root == None:
	    return 0
	return max(maxDepth(root.getLeft()), maxDepth(root.getRight())) + 1

def maxDepth(self, root):
	if root == None:
	    return 0
	q = []
	q.append([root, 1])
	temp = 0
	while len(q) != 0:
	    node, depth = q.pop()
	    depth = max(temp, dep)
	    if node.getLeft() != None:
		q.append([node.getLeft(), depth + 1])
	    if node.getRight() != None:
		q.append([node.getRight(), depth + 1])
	return temp
	
