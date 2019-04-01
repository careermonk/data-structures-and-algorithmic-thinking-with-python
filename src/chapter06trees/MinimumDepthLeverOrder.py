# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    def minimumDepth(self, root):
        if root is None:
            return 0
        queue = []
        queue.append((root, 1))
        while queue:
            current, depth = queue.pop(0)
            if current.left is None and current.right is None:
                return depth
            if current.left:
                queue.append((current.left, depth+1))
            if current.right:
                queue.append((current.right, depth+1))


tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
# tree.right = TreeNode(2)
# tree.right.right = TreeNode(3)
# tree.right.left = TreeNode(4)

temp = Solution()
print temp.minimumDepth(tree)
