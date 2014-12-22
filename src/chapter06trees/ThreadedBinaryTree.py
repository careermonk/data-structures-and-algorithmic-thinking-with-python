# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

'''Threaded Binary Tree Class and its methods'''
class ThreadedBinaryTree:
	def __init__(self, data):
		self.data = data  # data
		self.left = None  # left child
		self.LTag = None
		self.right = None  # right child
		self.RTag = None
		
def InorderSuccessor(P):
	if(P.RTag == 0): 
		return P.right
	else:	
		Position = P.right
		while(Position.LTag == 1):
			Position = Position.left
			return Position

def InorderTraversal(root):
	P = InorderSuccessor(root)
	while(P != root):
		P = InorderSuccessor(P)
		print P.data

def InorderTraversal(root):
	P = root
	while(1):	
		P = InorderSuccessor(P)
		if(P == root):
			return
		print P.data
		
def PreorderSuccessor(P):
	if(P.LTag == 1): 
		return P.left
	else :	
		Position = P
		while(Position.RTag == 0):
			Position = Position.right
		return Position.right
          
def PreorderTraversal(root):
	P = PreorderSuccessor(root)
	while(P != root) :
		P = PreorderSuccessor(P)
		print P.data
      
def PreorderTraversal(root) :
	P = root
	while(1):
		P = PreorderSuccessor(P)
		if(P == root): 
			return
		print P.data
      
# pre-order successor for an unthreaded binary tree
def PreorderSuccessor(node): 
	S = Stack()
	if(node != None): 
		P = node
	if(P.left != None): 
		Push(S, P)
		P = P.left
	else :   
		while (P.right == None):
			P = Pop(S)
			P = P.right
	return P

def InsertRightInInorderTBT(P, Q):
	Q.right = P.right
	Q.RTag = P.RTag
	Q.left = P
	Q.LTag = 0
	P.right = Q
	P.RTag = 1
	if(Q.RTag == 1) :  # Case-2
		Temp = Q.right
		while(Temp.LTag):
			Temp = Temp.left
		Temp.left = Q
      
# In-order successor for an unthreaded binary tree
def InorderSuccessor(node): 
	S = Stack()
	if(node != None): 
		P = node
	if(P.right == None): 
		P = Pop(S)
	else :	
		P = P.right
		while (P.left != None):
			Push(S, P)
		P = P.left
	return P





		
