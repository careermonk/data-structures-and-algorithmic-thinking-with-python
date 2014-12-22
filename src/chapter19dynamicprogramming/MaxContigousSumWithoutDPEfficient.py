# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def MaxContigousSum(A):
	sumSoFar = sumEndingHere = 0
	n = len(A)
	for i in range(0, n) :
		sumEndingHere = sumEndingHere + A[i]
		if(sumEndingHere < 0):
			sumEndingHere = 0
			continue
		if(sumSoFar < sumEndingHere):
			sumSoFar = sumEndingHere

	return sumSoFar


A = [-2, 3, -16, 100, -4, 5]
print MaxContigousSum(A)
A = [-2, 11, -4, 13, -5, 2 ]
print MaxContigousSum(A)
A = [-15, -23, -476, -3, -292]
print MaxContigousSum(A)
