# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def sumNumbers(self, root):
	if not root:
		return 0
	current = 0
	sum = [0]
	self.printPathsRecur(root, current, sum)
	return sum[0]
	
def printPathsRecur(self, root, current, sum):
	if not root:
		return
	current = current * 10 + root.data
	if not root.left and not root.right:
		sum[0] += current
		return

	self.printPathsRecur(root.left, current, sum)
	self.printPathsRecur(root.right, current, sum)
