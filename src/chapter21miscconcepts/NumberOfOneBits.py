# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def numberOfOnes1(n):
	count = 0
	while(n):
	     count += n & 1
	     n >>= 1
	print count

def numberOfOnes2(n):
	count = 0
	while(n):
	     if(n % 2 == 1):
		  count += 1
	     n = n / 2
	print count
	

def numberOfOnes3(n):
	count = 0
	while(n):
		count += 1
		n &= n - 1
	print count

def numberOfOnes4(n):
	Table = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
	count = 0
	while (n):
		count = count + Table[n & 0xF]
		n >>= 4
	print count

	

n = 11
numberOfOnes1(n)
numberOfOnes2(n)
numberOfOnes3(n)
numberOfOnes4(n)
