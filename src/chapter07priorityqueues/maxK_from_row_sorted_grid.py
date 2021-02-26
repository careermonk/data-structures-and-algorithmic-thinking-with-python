# Copyright (c) Feb 26, 2021 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2021-02-26 06:15:46 
# Last modification		: 2021-02-26 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

from queue import PriorityQueue


# Find smallest K elements from row-wise sorted grid

class MaxKFromGrid:
    def __init__(self, grid):
        self.grid = grid
    
    # TC: O(mlogm); SC: O(m) where m is the number of rows
    def findSmallestK(self, K):
        if K<=0 or not self.grid:
            return []
        
        heap = PriorityQueue()
        for i in range(len(self.grid)):
            heap.put((self.grid[i][0], i, 0))
        
        count = 0
        result = []
        while not heap.empty() and count<K:
            element, row, col = heap.get()
            result.append(element)
            
            count += 1
            
            if count == K:
                return result
            
            if count < K and col+1< len(self.grid[0]):
                    heap.put((self.grid[row][col+1], row, col+1))
        
        if count == K:
            return res  
            
grid =[[0,2,5,7,9],
     [-5,6,8,9,11],
     [4,5,10,13,16],
     [-4,0,5,8,19]]
obj = MaxKFromGrid(grid)
print(obj.findSmallestK(15))
