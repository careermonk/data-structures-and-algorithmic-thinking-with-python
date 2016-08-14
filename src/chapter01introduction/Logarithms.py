# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 


def logarithms(n):
	i = n
	while i >= 1: 
		i = i // 2
		print i	

logarithms(100)


def logarithms2(n):
	i = 1
	while i <= n: 
		i = i * 2
		print i	

logarithms(100)
