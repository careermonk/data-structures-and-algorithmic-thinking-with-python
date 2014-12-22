# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def checkPairwiseSorted(A):
	n = len(A)
	if (n == 0 or n == 1):
		return 1
	for i in range(0, n - 1, 2):	
		if (A[i] > A[i + 1]):
			return 0
	return 1


A = [34, 48, 10, 13, 2, 80, 30, 23]
print checkPairwiseSorted(A)
