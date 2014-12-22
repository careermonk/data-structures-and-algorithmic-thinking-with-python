# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def CountTrees(n) :
	if (n <= 1):   
		return 1
	else :	
		# there will be one value at the root, with whatever remains on the left and right
		# each forming their own subtrees. Iterate through all the values that could be the root...
		sum = 0
		for root in range(1, n + 1):
			left = CountTrees(root - 1)
			right = CountTrees(n - root)
			# number of possible trees with this root == left*right
			sum += left * right

		return(sum)
for i  in range(1, 11):
	print CountTrees(i)
