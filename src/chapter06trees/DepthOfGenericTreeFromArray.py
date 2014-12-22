# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def findDepthInGenericTree(P):
	maxDepth = -1
	currentDepth = -1
	for i in range (0, len(P)):
		currentDepth = 0
		j = i
		while(P[j] != -1):
		       currentDepth += 1
		       j = P[j]
		if(currentDepth > maxDepth):
			maxDepth = currentDepth
	
	return maxDepth

P = [-1, 0, 1, 6, 6, 0, 0, 2, 7]
print "Depth of given Generic Tree is:", findDepthInGenericTree(P)
