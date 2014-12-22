# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 


def Function(n):
	count = 0
	if n <= 0:
		return
	for i in range(1, n):
		j = 1
		while j < n:
			j = j + i
			count = count + 1
	print (count)

Function(20)

def Function2(n):
	for i in range(1, n):
		j = 1
		while j <= n:
			j = j * 2
			print("*")

Function2(20)

import math
def Function(n):
	for i in range(1, n / 3):
		j = 1
		while j <= n:
			j = j + 4
			print("*")

Function(20)
