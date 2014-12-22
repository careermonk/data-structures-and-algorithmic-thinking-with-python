# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def fillNextSiblings(root):
	if (root == None): 
		return

	if root.left: 
		root.left.nextSibling = root.right

	if roo.tright:
		if root.nextSibling:
			root.right.nextSibling = root.nextSibling.left 
		else:
			root.right.nextSibling = None

	fillNextSiblings(root.left)
	fillNextSiblings(root.right)
