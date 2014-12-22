# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def pathFinder(root, val, path, paths):
    if not root:
        return False
    
    if not root.left and not root.right:
        if root.data == val:
            path.append(root.data)
            paths.append(path)
            return True
        else:
            return False
    
    left = pathFinder(root.left, val - root.data, path + [root.data], paths)
    right = pathFinder(root.right, val - root.data, path + [root.data], paths)  # make sure it can be executed!
    return left or right


def hasPathWithSum(root, val):
    paths = []
    pathFinder(root, val, [], paths)
    print 'sum:', val
    print 'paths:', paths
