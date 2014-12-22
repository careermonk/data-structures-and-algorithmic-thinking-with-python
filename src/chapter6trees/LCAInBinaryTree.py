# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def lca(root, alpha, beta):
    if not root: return None
    if root.value == alpha or root.value == beta: return root
    left = lca(root.left, alpha, beta)
    right = lca(root.right, alpha, beta)
    if left and right: 
        # alpha & beta are on both sides
        return root
    else: 
        # EITHER alpha/beta is on one side 
        # OR alpha/beta is not in L&R subtrees
        return left if left else right
