# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def zigzagLevelOrder(self, root):
	result = []
	currentLevel = []
	if root != None:
	    currentLevel.append(root)
	leftToRight = True
	while len(currentLevel) > 0:
	    levelresult = []
	    nextLevel = []
	    while len(currentLevel) > 0:
		node = currentLevel.pop()
		levelresult.append(node.val)
		if leftToRight:
		    if node.left != None:
			nextLevel.append(node.left)
		    if node.right != None:
			nextLevel.append(node.right)
		else:
		    if node.right != None:
			nextLevel.append(node.right)
		    if node.left != None:
			nextLevel.append(node.left)
	    currentLevel = nextLevel
	    result.append(levelresult)
	    leftToRight = not leftToRight
	return result
