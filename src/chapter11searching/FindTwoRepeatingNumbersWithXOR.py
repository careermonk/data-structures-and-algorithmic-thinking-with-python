# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Approach is same for two repeated and two missing numbers
def findTwoRepeatingNumbersWithXOR (A):
	XOR = A[0]
	X = Y = 0
	n = len(A) - 2
	for i in range(1, len(A)):                   
		XOR ^= A[i]

	for i in range(1, n + 1):
		XOR ^= i   
 	rightMostSetBitNo = XOR & ~(XOR - 1)
	for i in range(0, len(A)):
		if(A[i] & rightMostSetBitNo):
			X = X ^ A[i]    
		else:	Y = Y ^ A[i]
	for i in range(1, n + 1):
		if(i & rightMostSetBitNo):
			X = X ^ i
		else:	Y = Y ^ i
 	print X, Y

A = [4, 2, 4, 5, 2, 3, 1]
findTwoRepeatingNumbersWithXOR(A)
