# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import heapq
class Heap:
	def __init__(self):
		self.heapList = [0]  # Elements in Heap
		self.size = 0  # Size of the heap
	def parent(self, index):
		"""
		Parent will be at math.floor(index/2). Since integer division
		simulates the floor function, we don't explicitly use it
		"""
		return index // 2
		
	def leftChildIndex(self, index):
		return 2 * index
		
	def rightChildIndex(self, index):
		return 2 * index + 1
		
	def leftChild(self, index):
		if 2 * index <= self.size:
			return self.heapList[2 * index ]
		return -1
		
	def rightChild(self, index):
		if 2 * index + 1 <= self.size :
			return self.heapList[2 * index + 1]
		return -1	

	def searchElement(self, itm):
		i = 1
		while (i <= self.size):
			if itm == self.heapList[i]:
				return i
			i += 1
	# Get Minimum for MinHeap
	def getMinimum(self):
	     if self.size == 0:
		  return -1
	     return self.heapList[1]

	def percolateDown(self, i):
	    while (i * 2) <= self.size:
		minimumChild = self.minimumChild(i)
		if self.heapList[i] > self.heapList[minimumChild]:
		    tmp = self.heapList[i]
		    self.heapList[i] = self.heapList[minimumChild]
		    self.heapList[minimumChild] = tmp
		i = minimumChild

	def minimumChild(self, i):
	    if i * 2 + 1 > self.size:
		return i * 2
	    else:
		if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
		    return i * 2
		else:
		    return i * 2 + 1

	def percolateUp(self, i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2

	# Delete Minimum for MinHeap
	def deleteMin(self):
	    retval = self.heapList[1]
	    self.heapList[1] = self.heapList[self.size]
	    self.size = self.size - 1
	    self.heapList.pop()
	    self.percolateDown(1)
	    return retval

	def insert(self, k):
		self.heapList.append(k)
		self.size = self.size + 1
		self.percolateUp(self.size)

	def printHeap(self):
		print self.heapList[1:]
		
	    
def FindKthLargestEle(HOrig, k):
	count = 1
	HAux = Heap()
	itm = HOrig.getMinimum()
	HAux.insert(itm)
	if count == k:
		return itm		
	while (HAux.size >= 1):
		itm = HAux.deleteMin()
		count += 1
		if count == k:
			return itm
		else:
			if HOrig.rightChild(HOrig.searchElement(itm)) != -1:
				HAux.insert(HOrig.rightChild(HOrig.searchElement(itm)))
			if HOrig.leftChild(HOrig.searchElement(itm)) != -1:	
				HAux.insert(HOrig.leftChild(HOrig.searchElement(itm)))

HOrig = Heap()
# add some nonsense:
HOrig.insert(1)
HOrig.insert(20)
HOrig.insert(5)
HOrig.insert(100)
HOrig.insert(1000)
HOrig.insert(12)
HOrig.insert(18)
HOrig.insert(16)

print FindKthLargestEle(HOrig, 6)
print FindKthLargestEle(HOrig, 3)
