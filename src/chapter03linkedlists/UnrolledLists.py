# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Node of a Singly Linked List
class Node:
	# constructor
	def __init__(self):
		self.value = None
		self.next = None

# Node of a Singly Linked List
class LinkedBlock:
	# constructor
	def __init__(self):
		self.head = None
		self.next = None
		nodeCount = 0
		
blockSize = 2
blockHead = None

# create an empty block
def newLinkedBlock():
	block = LinkedBlock()
	block.next = None
	block.head = None
	block.nodeCount = 0
	return block

# create a node 
def newNode(value):
	temp = Node()
	temp.next = None
	temp.value = value
	return temp

def searchElements(blockHead, k):
	# find the block 
	j = (k + blockSize - 1) // blockSize  # k-th node is in the j-th block 
	p = blockHead
	j -= 1
	while(j):
		p = p.next 
		j -= 1

	fLinkedBlock = p

	# find the node
	q = p.head
	k = k % blockSize
	if(k == 0):
		k = blockSize
	k = p.nodeCount + 1 - k
	k -= 1
	while (k):
		q = q.next
		k -= 1

	fNode = q
	
	return fLinkedBlock, fNode

# start shift operation from block *p 
def shift(A):
	B = A
	global blockHead	
	while(A.nodeCount > blockSize):  # if this block still have to shift
		if(A.next == None):  # reach the end. A little different
			A.next = newLinkedBlock()
			B = A.next
			temp = A.head.next
			A.head.next = A.head.next.next
			B.head = temp
			temp.next = temp
			A.nodeCount -= 1
			B.nodeCount += 1
		else:
			B = A.next
			temp = A.head.next			
			A.head.next = A.head.next.next	
			temp.next = B.head.next	
			B.head.next = temp		
			B.head = temp
			A.nodeCount -= 1			
			B.nodeCount += 1
        
	A = B

def addElement(k, x):
	global blockHead
	r = newLinkedBlock()
	p = Node() 

	if(blockHead == None):  # initial, first node and block
		blockHead = newLinkedBlock()
		blockHead.head = newNode(x)
		blockHead.head.next = blockHead.head
		blockHead.nodeCount += 1
	else:
		if(k == 0):  # special case for k=0. 
			p = blockHead.head
			q = p.next
			p.next = newNode(x)
			p.next.next = q
			blockHead.head = p.next
			blockHead.nodeCount += 1
			shift(blockHead)
		else:
			r, p = searchElements(blockHead, k)
			q = p
			while(q.next != p):
				q = q.next
			q.next = newNode(x)
			q.next.next = p
			r.nodeCount += 1
			shift(r)
        
	return blockHead
	
def searchElement(blockHead, k):
    q, p = searchElements(blockHead, k)
    return p.value


blockHead = addElement(0, 11)
blockHead = addElement(0, 21)
blockHead = addElement(1, 19)
blockHead = addElement(1, 23)
blockHead = addElement(2, 16)
blockHead = addElement(2, 35)
searchElement(blockHead, 1)
