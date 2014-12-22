# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def frequencyCounter(A):
	pos = 0
	n = len(A)
	while(pos < n):
		expectedPos = A[pos] - 1
		if(A[pos] > 0 and A[expectedPos] > 0):
			A[pos], A[expectedPos] = A[expectedPos], A[pos]
			A[expectedPos] = -1
		elif(A[pos] > 0):
			A[expectedPos] -= 1
			A[pos] = 0
			pos += 1
		else:
			pos += 1
	for i in range(1, n):
		print  i + 1 , "--->", abs(A[i])

A = [10, 1, 9, 4, 7, 6, 5, 5, 1, 2, 1]
frequencyCounter(A)
