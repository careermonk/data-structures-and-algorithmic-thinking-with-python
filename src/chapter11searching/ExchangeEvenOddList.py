# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def exchangeEvenOddList(head):
	# initializing the odd and even list headers
	oddList = evenList = None

	# creating tail variables for both the list
	oddListEnd = evenListEnd = None    
	itr = head	

	if(head == None):
		return
	else:
		while(itr != None):
			if(itr.data % 2 == 0):
				if(evenList == NULL):
					# first even node 
					evenList = evenListEnd = itr
				else:
					# inserting the node at the end of linked list                        
					evenListEnd.next = itr                           
					evenListEnd = itr
			else:
				if(oddList == NULL):
					# first odd node 
					oddList = oddListEnd = itr
				else:
					# inserting the node at the end of linked list
					oddListEnd.next = itr                          
					oddListEnd = itr
		itr = itr.next
	evenListEnd.next = oddList
	return head
