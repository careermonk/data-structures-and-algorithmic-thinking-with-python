# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class streamMedian: 
	def __init__(self): 
		self.minHeap, self.maxHeap = [], [] 
		self.n = 0   
	def insert(self, num): 
		if self.n % 2 == 0: 
			heapq.heappush(self.maxHeap, -1 * num) 
			self.n += 1 
			if len(self.minHeap) == 0: 
				return 
			if -1 * self.maxHeap[0] > self.minHeap[0]: 
				toMin = -1 * heapq.heappop(self.maxHeap) 
				toMax = heapq.heappop(self.minHeap) 
				heapq.heappush(self.maxHeap, -1 * toMax) 
				heapq.heappush(self.minHeap, toMin) 
			else: 
				toMin = -1 * heapq.heappushpop(self.maxHeap, -1 * num) 
				heapq.heappush(self.minHeap, toMin) 
				self.n += 1   
	def getMedian(self): 
		if self.n % 2 == 0: 
			return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2.0 
		else: 
			return -1 * self.maxHeap[0]
