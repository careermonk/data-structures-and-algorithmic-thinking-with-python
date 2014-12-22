# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

factTable = {}

def factorial(n):
    try:
        return factTable[n]
    except KeyError:
        if n == 0:
            factTable[0] = 1
            return 1
        else:
            factTable[n] = n * factorial(n - 1)
            return factTable[n]

print(factorial(10))
