# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def FindLargestInArray(A):
    max = 0
    for number in A:
        if number > max:
            max = number
    return max
	
print(FindLargestInArray([2, 1, 5, 234, 3, 44, 7, 6, 4, 5, 9, 11, 12, 14, 13]))
