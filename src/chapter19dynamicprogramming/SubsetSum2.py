# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def SubsetSum2(A):
	n = len(A)
	K = 0
	for i in range(0, n): 
		K += A[i]
	A.sort()
	T = [0] * (K + 1)
	T[0] = 1
	R = 0
	# process the numbers one by one
	for i in range(0, n): 
		for j in range(R, -1, -1): 
			if(T[j]): 
				T[j + A[i]] = 1
			R = min(K / 2, R + A[i])
	
	return T[K / 2]
	
A = [3, 2, 4, 19, 3, 7, 13, 10, 6, 11]

print SubsetSum2(A)
