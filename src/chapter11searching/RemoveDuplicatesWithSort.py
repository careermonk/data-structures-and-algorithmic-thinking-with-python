# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def RemoveDuplicates(A):
	A.sort()
	print A
	j = 0
	for i in range(1, len(A)):
		if (A[j] != A[i]):
			j += 1
			A[j] = A[i]
			
			
	print A[:j + 1]

A = [54, 31, 93, 54, 77, 31, 44, 55, 93]
RemoveDuplicates(A)
