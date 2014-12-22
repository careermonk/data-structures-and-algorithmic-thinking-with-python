# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def moveZerosToEnd(A):
	i = j = 0
	while (i <= len(A) - 1):  
		if (A[i] != 0):
			A[j] = A[i]
			j += 1
		i += 1
	while (j <= len(A) - 1):   
		A[j] = 0
		j += 1
	return A
A = [7, 0, 0, 3, 0, 2, 3, 3, 6, 3]
print A, "\n", moveZerosToEnd(A)

def mySwap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp

def moveZerosToEnd2(A):
	i = j = 0
	while (i <= len(A) - 1):  
		if (A[i] != 0):
			mySwap(A, j, i)
			j += 1
		i += 1
	return A

A = [7, 0, 0, 3, 0, 2, 3, 3, 6, 3]
print A, "\n", moveZerosToEnd2(A)
