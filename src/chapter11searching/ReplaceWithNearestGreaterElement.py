# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def replaceWithNearestGreaterElement(A):
	nextNearestGreater = float("-inf")
	i = j = 0
	for i in range(0, len(A) - 1):
		nextNearestGreater = float("-inf")
		for j in range(i + 1, len(A)):
			if A[i] < A[j]:
				nextNearestGreater = A[j]
				break
		print("For the element " + str(A[i]) + ", " + str(nextNearestGreater) + " is the nearest greater element")

replaceWithNearestGreaterElement([6, 2, 4, 1, 2, 1, 2, 2, 10])
