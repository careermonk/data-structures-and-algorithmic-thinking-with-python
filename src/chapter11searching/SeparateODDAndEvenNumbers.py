# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def separateEvenOdd(A):
	left = 0; right = len(A) - 1
	while(left < right):
		while(A[left] % 2 == 0 and left < right):
			left += 1
		while(A[right] % 2 == 1 and left < right):
			right -= 1
		if(left < right):
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
A = [12, 34, 45, 9, 8, 90, 3]
separateEvenOdd(A)
print A
