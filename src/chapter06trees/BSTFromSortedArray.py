# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 


class Node:
 ''' class to represent a Node of BST/ linked list'''
 def __init__(self, data=None):
     self.data = data
     self.left = None
     self.right = None

def printBST(root):
	'''prints the BST in an inorder sequence'''
	if not root:
		return
	else:
		printBST(root.left)
		print root.data, " ",
		printBST(root.right)

def printList(head):
 '''prints the linked list in both directions
  to test whether both the 'next' and 'previous' pointers are fine'''
 # print forward direction
 h = head
 print '[%d]' % (h.data),
 h = h.right
 while h != head:
     print '[%d]' % (h.data),
     h = h.right

 print ""
 # print in reverse direction
 h = head.left
 print '[%d]' % (h.data),
 h = h.left
 while h != head.left:
     print '[%d]' % (h.data),
     h = h.left

def  BuildBST(A, left, right) :
	if(left > right): 
		return None
	newNode = Node()
	if(not newNode) :
		print("Memory Error") 
		return

	if(left == right):
		newNode.data = A[left]
		newNode.left = None
		newNode.right = None	
	else :	
		mid = left + (right - left) / 2
		newNode.data = A[mid] 
		newNode.left = BuildBST(A, left, mid - 1)
		newNode.right = BuildBST(A, mid + 1, right)	
	return newNode

if __name__ == "__main__":
	# create the sample BST
	A = [2, 3, 4, 5, 6, 7]
	root = BuildBST(A, 0, len(A) - 1)
	print "\ncreating BST"
	printBST(root)
