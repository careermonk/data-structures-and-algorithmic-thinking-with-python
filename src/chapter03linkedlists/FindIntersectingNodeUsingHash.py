# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def findIntersectingNode(self, list1, list2):
	intersect = {}
	t = list1
	while None != t:
		intersect[t] = True
		t = t.getNext()

	# first duplicate is intersection
	t = list2
	while None != t:
		if None != intersect.get(t):
			return t
		t = t.getNext()
	return None
