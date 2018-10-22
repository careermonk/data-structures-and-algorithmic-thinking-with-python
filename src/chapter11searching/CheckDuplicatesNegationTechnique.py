# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import math
def CheckDuplicatesNegationTechnique(A):
	for i in range(0, len(A)):
		if(A[abs(A[i])] < 0):
			print("Duplicates exist:", A[i])
			return
		else:
			A[abs(A[i])] *= -1
			
	print("No duplicates in given array.")

A = [3, 2, 1, 2, 2, 3]
CheckDuplicatesNegationTechnique(A)
