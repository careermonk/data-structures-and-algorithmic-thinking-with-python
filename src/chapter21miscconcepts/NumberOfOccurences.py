# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def linear_search_count(A, data):
	count = 0
	for i in range (0, len(A)): 
		if(A[i] == data):
			count += 1
	return count

A = [7, 3, 6, 3, 3, 6, 7	]
print linear_search_count(A, 7)
