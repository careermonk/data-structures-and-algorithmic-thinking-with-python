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
 def __init__(self, data):
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
 if not head:
     return  
 if head: print head.data    
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


def BSTToDLL(root):
	''' main function to take the root of the BST and return the head of the doubly linked list  '''
	prev = None
	head = None
	BSTToDoublyList(root, prev, head)
	return head

def BSTToDoublyList(root, prev, head):
	if (not root): return 

	BSTToDoublyList(root.left, prev, head)

	# current node's left points to previous node
	root.left = prev
	if (prev):
		prev.right = root  # Previous node's right points to current node
	else:
		head = root  # If previous is NULL that current node is head

	right = root.right  # Saving right node

	# Now we need to make list created till now as circular
	head.left = root
	root.right = head

	# For right-subtree/parent, current node is in-order predecessor
	prev = root
	BSTToDoublyList(right, prev, head)
   

if __name__ == "__main__":
 # create the sample BST
 root = a = Node(5)
 b = Node(3)
 c = Node(6)
 d = Node(2)
 e = Node(4)
 f = Node(7)

 a.left, a.right = b, c
 b.left, b.right = d, e
 c.right = f

 printBST(root)

 print "\ncreating to double linked list"
 head = BSTToDLL(root)
 printList(head)
