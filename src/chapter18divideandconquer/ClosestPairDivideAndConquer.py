# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

from __future__ import generators

def ClosestPairWithDivideAndConquer(L):
	def square(x): 
		return x * x
	def sqdist(p, q): 
		return square(p[0] - q[0]) + square(p[1] - q[1])
	# We use the pair L[0],L[1] as our initial guess at a small distance.
	best = [sqdist(L[0], L[1]), (L[0], L[1])]
	
	# check whether pair (p,q) forms a closer pair than one seen already
	def testpair(p, q):
		d = sqdist(p, q)
		if d < best[0]:
			best[0] = d
			best[1] = p, q
			
	# merge two sorted lists by y-coordinate
	def merge(A, B):
		i = 0
		j = 0
		while i < len(A) or j < len(B):
			if j >= len(B) or (i < len(A) and A[i][1] <= B[j][1]):
				yield A[i]
				i += 1
			else:
				yield B[j]
				j += 1

	# Find closest pair recursively; returns all points sorted by y coordinate
	def recur(L):
		if len(L) < 2:
			return L
		split = len(L) / 2
		splitx = L[split][0]
		L = list(merge(recur(L[:split]), recur(L[split:])))

		# Find possible closest pair across split line
		# Note: this is not quite the same as the algorithm described in class, because
		# we use the global minimum distance found so far (best[0]), instead of
		# the best distance found within the recursive calls made by this call to recur().
		# This change reduces the size of E, speeding up the algorithm a little.
		#
		E = [p for p in L if abs(p[0] - splitx) < best[0]]
		for i in range(len(E)):
			for j in range(1, 8):
				if i + j < len(E):
					testpair(E[i], E[i + j])
		return L
	
	L.sort()
	recur(L)
	return best[1]

print ClosestPairWithDivideAndConquer([(12, 30), (40, 50), (5, 1), (12, 10), (3, 4)])
