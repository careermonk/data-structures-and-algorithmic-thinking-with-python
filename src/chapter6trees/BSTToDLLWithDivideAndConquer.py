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
     self.left = self
     self.right = self

def printBST(root):
 '''prints the BST in an inorder sequence'''
 if root.left == root or root.right == root:
     print root.data, " ",
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


def BSTToDLL(root):
 ''' main function to take the root of the BST and return the head of the doubly linked list  '''

 # for leaf Node return itself
 if root.left == root and root.right == root:
     return root

 elif root.left == root:  # no left subtree exist
     h2 = BSTToDLL(root.right)
     root.right = h2
     h2.left.right = root
     root.left = h2.left
     h2.left = root
     return root

 elif root.right == root:  # no right subtree exist
     h1 = BSTToDLL(root.left)
     root.left = h1.left
     h1.left.right = root
     root.right = h1
     h1.left = root
     return h1

 else:  # both left and right subtrees exist
     h1 = BSTToDLL(root.left)
     h2 = BSTToDLL(root.right)

     l1 = h1.left  # find last nodes of the lists
     l2 = h2.left

     h1.left = l2
     l2.right = h1

     l1.right = root
     root.left = l1

     root.right = h2
     h2.left = root
     return h1




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
 head = BSTToDLL(root);
 printList(head)
