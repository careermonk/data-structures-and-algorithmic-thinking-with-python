# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def power(k, n):
    if n == 0: return 1
    x = power(k, math.floor(n / 2))
    if n % 2 == 0: return pow(x, 2)
    else: return k * pow(x, 2)
	    
def powerBruteForce(k, n):
    """linear power algorithm"""
    x = k;
    for i in range(1, n):
        x *= k
    return x	    
