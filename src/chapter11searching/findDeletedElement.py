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
import random
import sys
 
def findDeletedElement1(A, B):
	for i in A:
		counter = 0
		for k in A:
			if (i == k):
				counter += 1
		for j in B:
			if (i == j):
				counter -= 1
		if (counter != 0):
			return i
	return sys.minint
 
def findDeletedElement2(A, B):
	A.sort()
	B.sort()
	for i in range(len(A)-1):
		if (A[i] != B[i]):
			return A[i]
	return A[len(A)-1]	
 
def findDeletedElement3(A, B):
	A.sort()
	B.sort()
	for a, b in zip(A, B):
		if (a != b):
			return a
	return A[len(A)-1]
 
def findDeletedElement4(A, B):
	h = defaultdict(int) # default value of int is 0
	for element in A:
		h[element] += 1
	for element in B:
		h[element] -= 1
	for element in A:
		if (h[element] >= 1):
			return element
 
def findDeletedElement5(A, B):
	return sum(A)-sum(B)
 
def findDeletedElement6(A, B):
	result = 0
	for i in A:
		result = result ^ i 
	for i in B:
		result = result ^ i 
	return result
 
def findDeletedElement7(A, B):
	result = 0
	for i, j in zip(A, B):
		result = result ^ i ^ j
	return result^A[len(A)-1]
 
A=[3,6,8,4,5,2,2,3]
print "Original A-->", A
random.shuffle(A)
print "A after shuffle-->", A
B=A[1:]
print "Original B-->", B
random.shuffle(B)
print "B after shuffle-->", B
#print findDeletedElement6(A, B)
print findDeletedElement7(A, B)
