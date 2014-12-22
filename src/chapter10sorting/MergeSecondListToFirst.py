# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def Merge(A, m, B, n):
	i = n - 1
	j = k = m - 1
	while k >= 0:
		if(B[i] > A[j] or j < 0):
			A[k] = B[i]
			i -= 1
			if(i < 0):
				break
		else:
			A[k] = A[j]
			j -= 1
		k -= 1
