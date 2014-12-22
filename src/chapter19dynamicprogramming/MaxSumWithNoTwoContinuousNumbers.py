# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def maxSumWithNoTwoContinuousNumbers(A):
	n = len(A)
	M = [0] * (n + 1)
	M[0] = A[0]
	
	if(A[0] > A[1]): 
		 M[0] = A[0]
	else: M[0] = A[1]
	for i in range(2, n): 
		if(M[i - 1] > M[i - 2] + A[i]):
			M[i] = M[i - 1]
		else: 	M[i] = M[i - 2] + A[i]	

	return M[n - 1]
	
A = [-2, 3, -16, 100, -4, 5]
print maxSumWithNoTwoContinuousNumbers(A)
A = [-2, 11, -4, 13, -5, 2 ]
print maxSumWithNoTwoContinuousNumbers(A)
A = [-15, -23, -476, -3, -292]
print maxSumWithNoTwoContinuousNumbers(A)
