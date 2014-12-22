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
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)

def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print root.data
    inOrderTraversal(root.right)

def preOrderTraversal(root):
    if not root:
        return        
    print root.data
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)    

r = Node(3)
insertNode(r, Node(7))
insertNode(r, Node(1))
insertNode(r, Node(5))

print "in order:"
inOrderTraversal(r)

print "pre order"
preOrderTraversal(r)
