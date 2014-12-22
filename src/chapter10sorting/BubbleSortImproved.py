# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def BubbleSort(A):
	swapped = 1 
	for i in range(len(A)):
		if (swapped == 0):
			return
		
		for k in range(len(A) - 1, i, -1):
			if (A[k] < A[k - 1]):
				swap(A, k, k - 1)
				swapped = 1

def swap(A, x, y):
	temp = A[x]
	A[x] = A[y]
	A[y] = temp
	

A = [127, 220, 246, 277, 321, 454, 534, 565, 933]
BubbleSort(A)
print(A) 
