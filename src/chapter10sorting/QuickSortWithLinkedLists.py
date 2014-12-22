# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.data = x
		self.next = None

def Qsort(first, last):
	lesHEAD = lesTAIL = None
	equHEAD = equTAIL = None
	larHEAD = larTAIL = None
	current = first
	if(current == None):
		return
	pivot = current.data
	Append(current, equHEAD, equTAIL)
	while (current != None):
		info = current.data
		if(info < pivot):
			Append(current, lesHEAD, lesTAIL)
		elif(info > pivot):
			Append(current, larHEAD, larTAIL)
		else:
			Append(current, equHEAD, equTAIL)
	
	Quicksort(lesHEAD, lesTAIL)
	Quicksort(larHEAD, larTAIL)
	Join(lesHEAD, lesTAIL, equHEAD, equTAIL)
	Join(lesHEAD, equTAIL, larHEAD, larTAIL)
	first = lesHEAD
	last = larTAIL
