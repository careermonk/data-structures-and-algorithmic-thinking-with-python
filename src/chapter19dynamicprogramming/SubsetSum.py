# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def positiveSubsetSum(A, X):
	# preliminary
	if X < 0 or X > sum(A):  # T = sum(A)
		return False

	# algorithm
	subSum = [False] * (X + 1)
	subSum[0] = True
	p = 0
	while not subSum[X] and p < len(A):
		a = A[p]
		q = X
		while not subSum[X] and q >= a:
			if not subSum[q] and subSum[q - a]:
				subSum[q] = True
			q -= 1
		p += 1
	return subSum[X]
