# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def getIntersectionNode(self, list1, list2):
	currentList1, currentList2 = list1, list2
	list1Len, list2Len = 0, 0
	while currentList1 is not None:
	    list1Len += 1
	    currentList1 = currentList1.next
	while currentList2 is not None:
	    list2Len += 1
	    currentList2 = currentList2.next
	currentList1, currentList2 = list1, list2
	if list1Len > list2Len:
	    for i in range(list1Len - list2Len):
		currentList1 = currentList1.next
	elif list2Len > list1Len:
	    for i in range(list2Len - list1Len):
		currentList2 = currentList2.next
	while currentList2 != currentList1:
	    currentList2 = currentList2.next
	    currentList1 = currentList1.next
	return currentList1
