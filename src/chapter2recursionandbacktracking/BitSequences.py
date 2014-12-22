# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 


def appendAtBeginningFront(x, L):
	return [x + element for element in L]

def bitStrings(n):
    if n == 0: return []
    if n == 1: return ["0", "1"]
    else:
        return (appendAtBeginningFront("0", bitStrings(n - 1)) + appendAtBeginningFront("1", bitStrings(n - 1)))
                
print bitStrings(4)                      

def bitStrings2(n):
	if n == 0: return []
	if n == 1: return ["0", "1"]
	return [ digit + bitstring for digit in bitStrings2(1)
	                         for bitstring in bitStrings2(n - 1)]
print bitStrings2(4)                      
