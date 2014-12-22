# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class Answer:
    def maxPathSum(self, root):
        self.maxValue = float("-inf")
        self.maxPathSumRec(root)
        return self.maxValue
    
    def maxPathSumRec(self, root):
        if root == None:
             return 0
        leftSum = self.maxPathSumRec(root.left)
        rightSum = self.maxPathSumRec(root.right)
        if leftSum < 0 and rightSum < 0:
            self.maxValue = max(self.maxValue, root.val)
            return root.val
        if leftSum > 0 and rightSum > 0:
            self.maxValue = max(self.maxValue, root.val + leftSum + rightSum)
        maxValueUp = max(leftSum, rightSum) + root.val
        self.maxValue = max(self.maxValue, maxValueUp)
        return maxValueUp
