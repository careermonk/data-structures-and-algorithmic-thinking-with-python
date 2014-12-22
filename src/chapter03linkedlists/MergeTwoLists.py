# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def mergeTwoLists(self, list1, list2):
	temp = Node()
	pointer = temp
	while list1 != None and list2 != None:
	    if list1.getData() < list2.getData():
		pointer.setNext(list1)
		list1 = list1.getNext()
	    else:
		pointer.setNext(list2)
		list2 = list2.getNext()
	    pointer = pointer.getNext()
	if list1 == None:
	    pointer.setNext(list2)
	else:
	    pointer.setNext(list1)
	return temp.getNext()
