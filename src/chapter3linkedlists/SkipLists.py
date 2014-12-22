# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import random
import math

class Node(object):
    def __init__(self, data, level=0):
        self.data = data
        self.next = [None] * level
    
    def __str__(self):
        return "Node(%s,%s)" % (self.data, len(self.next))
    __repr__ = __str__
    
class SkipList(object):
    def __init__(self, max_level=8):
        self.max_level = max_level
        n = Node(None, max_level)
        self.head = n
        self.verbose = False

    def randomLevel(self, max_level):
        num = random.randint(1, 2 ** max_level - 1)
        lognum = math.log(num, 2)
        level = int(math.floor(lognum))
        return max_level - level
    
    def updateList(self, data):
        update = [None] * (self.max_level)
        n = self.head
        
        self._n_traverse = 0
        
        level = self.max_level - 1
        while level >= 0:
            if self.verbose and \
                n.next[level] != None and n.next[level].data >= data:
                print 'DROP down from level', level + 1
            while n.next[level] != None and n.next[level].data < data:
                self._n_traverse += 1
                if self.verbose:
                    print 'AT level', level, 'data', n.next[level].data
                n = n.next[level]
            update[level] = n
            level -= 1

        return update
    
    def find(self, data, update=None):
        if update is None:
            update = self.updateList(data)
                        
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate != None and candidate.data == data:
                return candidate
        return None
    
    def insertNode(self, data, level=None):
        if level is None:
            level = self.randomLevel(self.max_level)
            
        node = Node(data, level)
        
        update = self.updateList(data)
        if self.find(data, update) == None:
            for i in range(level):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
    
def printLevel(sl, level):
    print 'level %d:' % level,
    node = sl.head.next[level]
    while node:
        print node.data, '=>',
        node = node.next[level]
    print 'END'

x = SkipList(4)
for i in range(0, 20, 2):
    x.insertNode(i)

printLevel(x, 0)
printLevel(x, 1)
printLevel(x, 2)
