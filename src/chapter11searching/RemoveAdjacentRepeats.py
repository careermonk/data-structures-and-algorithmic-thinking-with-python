# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def removeAdjacentRepeats(nums):
  i = 1
  while i < len(nums):    
    if nums[i] == nums[i - 1]:
      nums.pop(i)
      i -= 1  
    i += 1
  return nums
  
nums = ["A", "B", "C", "C", "C", "C", "B", "A"]  
print removeAdjacent(nums)
