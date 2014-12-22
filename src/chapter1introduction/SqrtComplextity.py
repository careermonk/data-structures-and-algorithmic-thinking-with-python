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
	i = s = 1
	while  s < n:
		i = i + 1
		s = s + i
		print("*")


Function(20)

def Function2(n):
	i = 1
	count = 0
	while i * i < n:
		count = count + 1
		i = i + 1
	print(count)

Function2(20)
