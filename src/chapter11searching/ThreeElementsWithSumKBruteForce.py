# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def threeElementsWithSumKBruteForce(A, K):
	n = len(A)
    	for i in range(0, n - 2):
		for j in range(i + 1, n - 1):
			for k in range(j + 1, n):
				if(A[i] + A[j] + A[k] == K):
					print "yes-->", A[i], " + ", A[j], " + ", A[k], " = ", K		
					return 1
	return 0    
A = [1, 6, 45, 4, 10, 18]
A.sort()
threeElementsWithSumKBruteForce(A, 22)
