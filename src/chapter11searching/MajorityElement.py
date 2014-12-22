# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def majorityElement(A):
	count = 0
	element = -1
	n = len(A)
	if n == 0:
		return
	for i in range(0, n - 1):
		if(count == 0) :
			element = A[i]
			count = 1
		elif(element == A[i]):
			count += 1
		else:
			count -= 1
	return element

A = [7, 3, 2, 3, 3, 6, 3	]
print majorityElement(A)
