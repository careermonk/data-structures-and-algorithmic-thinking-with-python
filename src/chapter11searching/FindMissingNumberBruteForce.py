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
	for i in range(1, n + 1):
		found = 0
		for j in range(0, n):
			if(i == A[j]):
				found = 1
		if found == 0:
			print "Missing number is ", i

A = [8, 2, 1, 4, 6, 5, 7, 9]
FindMissingNumber(A)
