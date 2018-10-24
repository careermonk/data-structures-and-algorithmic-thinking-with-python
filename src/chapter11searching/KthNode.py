# Copyright (c) Oct 22, 2018 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 
class Node:
	def __init__(self, data = None):
		self.data = data
		self.next = None
 
class LinkedList:
	def __init__(self, node = None):
		self.head = node
	def length(self):
		count = 0
		temp = self.head
		while temp:
			count += 1
			temp = temp.next
		return count
	def findKthBruteForce(self, K):
		length = ll.length()
		c = 0
		temp = ll.head
		while (c<(length-K)):
			temp = temp.next
			c += 1
		return temp
	def findKthHashing(self, K):
		h = {}
		c = 1
		temp = ll.head
		while (temp):
			h[c] = temp 
			temp = temp.next
			c += 1
		return h[c-K]
	def findKthEfficient(self, K):
		v1 = ll.head
		while (K and v1):
			v1 = v1.next
			K -= 1
		if K:
			return None

		v2 = ll.head
		while(v1):
			v1 = v1.next
			v2 = v2.next
		return v2	
 
node1 = Node(10)
node2 = Node(2)
node3 = Node(6)
node4 = Node(8)
node5 = Node(3)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
 
ll = LinkedList(node1)
kthNode = ll.findKthEfficient(20)
if kthNode:
	print kthNode.data
else:
	print "Check the list...seems K is greater than n"
