# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def PrintAllAncestors(root, node):
	if(root == NULL):
		return 0
	if(root.left == node or root.right == node or  PrintAllAncestors(root.left, node) or PrintAllAncestors(root.right, node)):
		print(root.data)
		return 1
	return 0
