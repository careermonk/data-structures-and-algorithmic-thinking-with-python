# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 


def rangeToList(k):
	result = []
	for i in range(0, k):
		result.append(str(i))
	return result
	
def BaseKStrings(n, k):
	if n == 0: return []
	if n == 1: return rangeToList(k)
	return [ digit + bitstring for digit in BaseKStrings(1, k)
	                         for bitstring in BaseKStrings(n - 1, k)]
print BaseKStrings(4, 3)    
