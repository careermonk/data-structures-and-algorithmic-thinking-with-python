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
def power_brute_force(k, n):
	"""linear power algorithm"""
	x = k
	for i in range(1, n):
	    x *= k
	return x

print power_brute_force(2, 3)

	    

def power_divide_and_conquer(k, n):
"""Divide and Conquer power algorithm"""

	# base case
	if n == 0: 
		return 1

	# base case
	if k == 0:
		return 0

	x = power_divide_and_conquer(a, math.floor(n/2))
	if n % 2 == 0: 
		return x * x
	else: 
		return k * x * x

print power_divide_and_conquer(2, 4)
    
