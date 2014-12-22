# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def FindMissingNumber(A):
	n = len(A)
	X = 0
	for i in range(1, n + 2):
		X = X ^ i
	for i in range(0, n):
		X = X ^ A[i]
	print "Missing number is ", X
A = [8, 2, 1, 4, 6, 5, 7, 9]
FindMissingNumber(A)
