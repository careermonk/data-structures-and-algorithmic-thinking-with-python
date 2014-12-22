# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def twoElementsWithSumKBruteForce(A, K):
	n = len(A)
    	for i in range(0, n):
		for j in range(i + 1, n):
			if(A[i] + A[j] == K):
				return 1
	return 0
    
A = [1, 4, 45, 6, 10, -8]
A.sort()
print twoElementsWithSumKBruteForce(A, 111)
