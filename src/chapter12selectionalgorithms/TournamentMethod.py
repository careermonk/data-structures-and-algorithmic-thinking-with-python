# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def secondSmallestInArray(A):
	comparisonCount = 0
	# indexes that are to be compared    
	idx = range(0, len(A))

	# list of knockout for all elements
	knockout = [[] for i in idx]
	# play tournaments, until we have only one node left
	while len(idx) > 1:   
	    # index of nodes that win this tournament
	    idx1 = []
	    # nodes in idx odd, if yes then last automatically goes to next round
	    odd = len(idx) % 2
	    # iterate over even indexes, as we do a paired tournament
	    for i in xrange(0, len(idx) - odd, 2):
		firstIndex = idx[i]
		secondIndex = idx[i + 1]
		comparisonCount += 1
		# perform tournament
		if A[firstIndex] < A[secondIndex]:
		    # firstIndex qualifies for next round
		    idx1.append(firstIndex)
		    # add A[secondIndex] to knockout list of firstIndex
		    knockout[firstIndex].append(A[secondIndex])
		else:
		    idx1.append(secondIndex)
		    knockout[secondIndex].append(A[firstIndex])

	    if odd == 1:
		idx1.append(idx[i + 2])
	    # perform new tournament
	    idx = idx1
	print "Smallest element =", A[idx[0]]
	print "Total comparisons =", comparisonCount
	print "Nodes knocked off by the smallest =", knockout[idx[0]], "\n"
	# compute second smallest
	a = knockout[idx[0]]
	if len(a) > 0:
	    v = a[0]
	    for i in xrange(1, len(a)):
		comparisonCount += 1
		if v > a[i]: v = a[i]

	    print "Second smallest element =", v
	    print "Total comparisons =", comparisonCount

A = [2, 4, 3, 7, 3, 0, 8, 4, 11, 1]	
print(secondSmallestInArray(A))	
