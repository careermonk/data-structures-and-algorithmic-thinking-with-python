# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def AreMirrors(root1, root2):
	if(root1 == None and root2 == None): 	
		return 1
	if(root1 == None or root2 == None): 
		return 0
	if(root1.data != root2.data): 	
		return 0
	else:
		return AreMirrors(root1.left, root2.right) and AreMirrors(root1.right, root2.left)
