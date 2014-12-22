# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def MaxRepititionsBruteForce(A):
	n = len(A)
	count = max = 0
	for i in range(0, n):
		count = 1
		for j in range(0, n):
			if(i != j and A[i] == A[j]):
				count += 1
		if max < count:
			max = count
			maxRepeatedElement = A[i]
	print maxRepeatedElement, "repeated for ", max

A = [3, 2, 1, 2, 2, 3, 2, 1, 3]
MaxRepititionsBruteForce(A)
