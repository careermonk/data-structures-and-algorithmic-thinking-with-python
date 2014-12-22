# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def treeMaximumSumPath(node, is_left=True, Lpath={}, Rpath={}):
    if is_left:
        # left sub-tree
        if not node.left:
            Lpath[node.id] = 0
            return 0
        else:
            Lpath[node.id] = node.data + max(
                treeMaximumSumPath(node.left, True, Lpath, Rpath),
                treeMaximumSumPath(node.left, False, Lpath, Rpath)
            )
            return Lpath[node.id]
    else:
        # right sub-tree
        if not node.right:
            Rpath[node.id] = 0
            return 0
        else:
            Rpath[node.id] = node.data + max(
                treeMaximumSumPath(node.right, True, Lpath, Rpath),
                treeMaximumSumPath(node.right, False, Lpath, Rpath)
            )
            return Rpath[node.id]


def maxsum_path(root):
    Lpath = {}
    Rpath = {}
    treeMaximumSumPath(root, True, Lpath, Rpath)
    treeMaximumSumPath(root, False, Lpath, Rpath)
    print 'Left-path:', Lpath
    print 'Right-path:', Rpath
    path2sum = dict((i, Lpath[i] + Rpath[i]) for i in Lpath.keys())
    i = max(path2sum, key=path2sum.get)
    print 'The path going through node', i, 'with max sum', path2sum[i]
    return path2sum[i]
