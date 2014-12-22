# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def deleteLinkedListDuplicates(self):
	current = self.head;
	while current != None and current.next != None:
	    if current.getData() == current.getNext().getData():
		current.setNext(current.getNext().getNext())
	    else:
		current = current.getNext()
	return head
