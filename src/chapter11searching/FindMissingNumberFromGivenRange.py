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
def findMissingNumberFromGivenRange(A, X, Y):
	n = len(A)
	S = [-sys.maxint] * (n)
	missingNum = -sys.maxint
	for i in range(0, n):
		S[A[i] - X] = A[i]
	for i in range(0, n):
		if(S[i] == -sys.maxint):
			missingNum = i + X
			break
	return missingNum		
A = [10, 16, 14, 12, 11, 10, 13 , 15, 17, 12, 19]
print findMissingNumberFromGivenRange(A, 10, 20)
