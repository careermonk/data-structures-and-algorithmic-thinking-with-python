# Copyright (c) Oct 22, 2018 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def findPivot1(A):
	for i in range(len(A)):
		leftSum = sum(A[:i])
		rightSum = sum(A[i+1:])
		if leftSum == rightSum:
			return A[i]

def findPivot2(A):
	S= sum(A)
	leftSum = 0
	for i in range(len(A)):
		if leftSum == S-A[i]-leftSum:
			return A[i]		
		leftSum += A[i]

print findPivot2([12,6,9,3,5,2,1,9,10])
