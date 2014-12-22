# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import sys
def minJumps(A):
	n = len(A)
	jumps = [0] * (n)
	if (n == 0 or A[0] == 0):
		return sys.maxint + 1

	jumps[0] = 0
	for i in range(1, n):
		jumps[i] = sys.maxint + 1
		for j in range(0, i):
			if (i <= j + A[j] and jumps[j] != sys.maxint + 1):
				jumps[i] = min(jumps[i], jumps[j] + 1)
				break
	return jumps[n - 1]

A = [1, 3, 6, 1, 0, 9]
print "Minimum number of jumps to reach end is ", minJumps(A)

A = [2, 3, 1, 1, 4]
print "Minimum number of jumps to reach end is ", minJumps(A)
