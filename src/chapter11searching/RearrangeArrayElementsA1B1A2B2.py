# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def rearrangeArrayElementsA1B1A2B2(A):
	n = len(A) // 2
	i = 0; 	q = 1; k = n
	while (i < n):
		
		j = k
		while j > i + q:
			A[j], A[j - 1] = A[j - 1], A[j]
			j -= 1
		i += 1; k += 1; q += 1

A = [1, 3, 5, 6, 2, 4, 6, 8]
rearrangeArrayElementsA1B1A2B2(A)
print A
