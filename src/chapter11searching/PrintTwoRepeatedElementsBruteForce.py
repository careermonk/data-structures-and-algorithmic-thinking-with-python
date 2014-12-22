# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

  
def PrintTwoRepeatedElementsBruteForce(A):
	n = len(A)
	for i in range(0, n):
		for j in range(i + 1, n):
			if(A[i] == A[j]):
				print A[i]


A = [3, 5, 7, 4, 2, 4, 2, 1, 9]
PrintTwoRepeatedElementsBruteForce(A)
