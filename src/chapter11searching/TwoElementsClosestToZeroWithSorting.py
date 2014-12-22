# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import sys
def TwoElementsClosestToZero(A):
	n = len(A)
	A.sort()
	if(n < 2):
		print "Invalid Input"
		return
	l = 0
	r = n - 1		
 	minLeft = l
	minRight = n - 1
	minSum = sys.maxint
	while(l < r):
		sum = A[l] + A[r];
		if(abs(minSum) > abs(sum)):
			minSum = sum
			minLeft = l
			minRight = r
		if sum < 0:
			l += 1
		else: r -= 1
	print " The two elements whose sum is minimum are ", A[minLeft], A[minRight]

A = [1, 60, -10, 70, -80, 85]
TwoElementsClosestToZero(A)
A = [10, 8, 3, 5, -9, -7, 6]
TwoElementsClosestToZero(A)
