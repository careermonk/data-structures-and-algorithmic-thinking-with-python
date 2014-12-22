# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def findingSpans(A):
	s = [None] * len(A)
	for i in range(0, len(A)):
		j = 1					
		while j <= i and A[i] > A[i - j]:
		       j = j + 1			                     
		s[i] = j	    		 	
	print s

findingSpans(['6', '3', '4', '5', '2'])
