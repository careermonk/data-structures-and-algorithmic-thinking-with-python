# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def MaxRepititionsEfficient(A):
	n = len(A)
	max = 0
	for i in range(0, len(A)):
		A[A[i] % n] += n
	for i in range(0, len(A)):
		 if(A[i] / n > max): 
			max = A[i] / n
			maxIndex = i
	print maxIndex, "repeated for ", max, " times"
A = [3, 2, 2, 3, 2, 2, 2, 3, 3]
MaxRepititionsEfficient(A)
