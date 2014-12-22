# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def SubsetSum(A, T):
	n = len(A)
	M = [[0 for x in range(T + 1)] for x in range(n + 1)]

	M[0][0] = 0
	for i in range(0, n + 1): 	
		M[i][0] = 0
	for i in range(0, T + 1): 	
		M[0][i] = 0		
	for i in range(1, n + 1): 	
		for j in range(1, T + 1): 	
			M[i][j] = M[i - 1][j] or (M[i - 1][j - A[i]])
	return M[n][T]

A = [3, 2, 4, 19, 3, 7, 13, 10, 6, 11]

print SubsetSum(A, 17)
