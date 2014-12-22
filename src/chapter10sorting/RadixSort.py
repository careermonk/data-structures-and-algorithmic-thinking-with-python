# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

	def RadixSort(A):
	  RADIX = 10
	  maxLength = False
	  tmp , placement = -1, 1
	 
	  while not maxLength:
		maxLength = True
		buckets = [list() for _ in range(RADIX)]
		for  i in A:
			tmp = i / placement
			buckets[tmp % RADIX].append(i)
			if maxLength and tmp > 0:
				maxLength = False
	 
		a = 0
		for b in range(RADIX):
			buck = buckets[b]
			for i in buck:
				A[a] = i
				a += 1
	 
		# move to next digit
		placement *= RADIX
	  
	A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
	print(RadixSort(A))
