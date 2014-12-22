# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import string
import collections
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
	
STRIP = string.whitespace + string.punctuation + "\"'"
def palindromeCheckerWithDeque(str1):
	d1 = Deque()
	d2 = collections.deque()
	for s in str1.lower():
		if s not in STRIP:
			d2.append(s)
			d1.addRear(s)
	eq1 = True
	while d1.size() > 1 and eq1:
		if d1.removeFront() != d1.removeRear():
			eq1 = False

	eq2 = True
	while len(d2) > 1 and eq2:
		if d2.pop() != d2.popleft():
			eq2 = False
		
	return eq1, eq2

str1 = 'Madam Im Adam'
str2 = 'Buffy is a Slayer'
print(palindromeCheckerWithDeque(str1))
print(palindromeCheckerWithDeque(str2))
