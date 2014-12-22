# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def rangePrinter(root, K1, K2): 
	if not root: 
		return 
	if K1 <= root.getData() <= K2: 
		print(root.getData())
	if root.getData() < K1: 
		return rangePrinter(root.getRight()) 
	if root.getData() > K2: 
		return rangePrinter(root.getLeft())


import Queue
def rangePrinter(root):
	if root is None:
		return

	q = Queue.Queue()
	q.put(root)
	temp = None

	while not q.empty():
		temp = q.get()  # dequeue FIFO
		if K1 <= root.getData() <= K2: 
			print(root.getData())
		if temp.getLeft() is not None and temp.getData() >= K1:
			q.put(temp.getLeft())
		if temp.getRight() is not None and temp.getData() <= K2:
			q.put(temp.getRight())	

	
