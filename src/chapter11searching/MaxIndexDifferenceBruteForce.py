# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def maxIndexDiff(A):
	maxDiff = -1
	maxJ = maxI = -1
	n = len(A)
	for i in range(0, n):
		j = n - 1
		while(j > i):
			if(A[j] > A[i] and maxDiff < (j - i)):
				maxDiff = j - i
				maxI = i
				maxJ = j
			j -= 1
	return maxDiff, maxI, maxJ
	
A = [34, 8, 10, 3, 2, 80, 30, 33, 1]
print maxIndexDiff(A)
