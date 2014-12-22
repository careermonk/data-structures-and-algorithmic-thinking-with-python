# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def MaxRepititionsWithSort(A):
	A.sort()
	print A
	j = 0
	count = max = 1
	element = A[0]
	for i in range(1, len(A)):
		if (A[i] == element):
			count += 1
			if count > max:
				max = count
				maxRepeatedElement = element
		else:
			count = 1
			element = A[i]
			
	print maxRepeatedElement, "repeated for ", max

A = [3, 2, 1, 3, 2, 3, 2, 3, 3]
MaxRepititionsWithSort(A)
