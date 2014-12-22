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
	n = len(A)
	LeftMins = [0] * (n)
	RightMaxs = [0] * (n)
	LeftMins[0] = A[0]
	for i in range(1, n):
		LeftMins[i] = min(A[i], LeftMins[i - 1])

	RightMaxs[n - 1] = A[n - 1]
	for j in range(n - 2, -1, -1):
		RightMaxs[j] = max(A[j], RightMaxs[j + 1])

	i = 0; j = 0; maxDiff = -1;
	while (j < n and i < n):
		if (LeftMins[i] < RightMaxs[j]):
			maxDiff = max(maxDiff, j - i)
			j = j + 1
		else:
			i = i + 1
	return maxDiff

A = [34, 8, 10, 3, 2, 80, 30, 33, 1]
print maxIndexDiff(A)
