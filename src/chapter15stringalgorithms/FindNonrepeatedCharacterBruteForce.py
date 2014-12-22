# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def findNonrepeated(A):
	n = len(A)
	for i in range(0, n):
		repeated = 0
		for j in range(0, n):
			if(i != j and A[i] == A[j]):
				repeated = 1
		if repeated == 0:
			return A[i]
	return
		
print findNonrepeated("careermonk")
