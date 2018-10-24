# Copyright (c) Oct 22, 2018 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 
from collections import defaultdict
def twoElementsWithSumK1(A, K):
	n = len(A)
	for i in range(n):
		for j in range(i + 1, n):
			if(A[i] + A[j] == K):
				print ("%d=%d+%d" %(K, A[i], A[j]))
 
def twoElementsWithSumK2(A, K):
	A.sort()
	i = 0
	j = len(A)-1
	while(i<=j):
		if(A[i] + A[j] == K):
			print ("%d=%d+%d" %(K, A[i], A[j]))
			i += 1
		elif(A[i] + A[j] > K):
			j -= 1
		else:
			i += 1
 
def twoElementsWithSumK3(A, K):
	h = defaultdict(int) # default value of int is 0
 	for element in A:
		h[element] += 1
		if(h[K - element]):
			if ((K - element) == element and h[element] == 1):
				continue
			else:
				print ("%d=%d+%d" %(K, element, K - element))
 
A = [1,2,3,1,4,5,2,6,2,5,6]
print twoElementsWithSumK3(A, 10)
