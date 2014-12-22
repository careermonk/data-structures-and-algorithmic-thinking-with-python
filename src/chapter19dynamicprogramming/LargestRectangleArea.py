# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def largestRectangleArea(self, height):
	stack = []; i = 0; maxArea = 0
	while i < len(height):
	    if stack == [] or height[i] > height[stack[len(stack) - 1]]:
		stack.append(i)
	    else:
		curr = stack.pop()
		width = i if stack == [] else i - stack[len(stack) - 1] - 1
		maxArea = max(maxArea, width * height[curr])
		i -= 1
	    i += 1
	while stack != []:
	    curr = stack.pop()
	    width = i if stack == [] else len(height) - stack[len(stack) - 1] - 1
	    maxArea = max(maxArea, width * height[curr])
	return maxArea
