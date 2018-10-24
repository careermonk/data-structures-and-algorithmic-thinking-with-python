# Copyright (c) Oct 22, 2018 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import random 

class Queue:
    def __init__(self):
        self.array = []
    def size(self):
        return len(self.array)
    def isEmpty(self):
        return len(self.array) == 0
    def front(self):
        if self.isEmpty():
            return None
        return self.array[0]
    def dequeue(self):
        if self.isEmpty():
            print "Underflow"
            return None
        data = self.array[0]
        self.array.remove(data)
        return data
    def enqueue(self, data):
        self.array.append(data)

def testQueue():
    q = Queue()
    c = 5
    while(c):
        data = random.randrange(1,100)
        print "Enqueuing ", data
        q.enqueue(data)
        c -= 1
    print "Queue size ", q.size()
    c = 5
    while(c):
        print "Dequeueing", q.dequeue()
        c -= 1

print testQueue()
