# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Search the key from node, iteratively
def Find(self, root, data):
	currentNode = root
	while currentNode:
	    if data == currentNode.get_data():
		return currentNode
	    if key < currentNode.get_data():
		currentNode = currentNode.getLeft()
	    else:
		currentNode = currentNode.getRight()
	return None
