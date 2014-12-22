# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class BloomFilter:
 """ Bloom Filter """
 def __init__(self, m, k, hashFun):
	self.m = m
	self.vector = [0] * m
	self.k = k
	self.hashFun = hashFun
	self.data = {}  # data structure to store the data
	self.flasePositive = 0

 def insert(self, key, value):
	self.data[key] = value
	for i in range(self.k):
		self.vector[self.hashFun(key + str(i)) % self.m] = 1

 def contains(self, key):
	for i in range(self.k):
		if self.vector[self.hashFun(key + str(i)) % self.m] == 0:
			return False  # the key doesn't exist
	return True  # the key can be in the data set

 def get(self, key):
	if self.contains(key):
		try:
			return self.data[key]  # actual lookup
		except KeyError:
			self.flasePositive += 1
    
import hashlib
def hashFunction(x):
	h = hashlib.sha256(x)  # we'll use sha256 just for this example
	return int(h.hexdigest(), base=16)

b = BloomFilter(100, 10, hashFunction)
b.insert('this is a test key', 'this is a new value')
print b.get('this is a key')    
print b.get('this is a test key')    
