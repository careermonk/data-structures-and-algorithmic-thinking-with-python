# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def reverseKBlock(self, head, k):
        temp = Node(0);
        temp.setNext(head)
        previous = temp
        while True:
            begin = previous.getNext()
            end = previous
            for i in range(0, k):
                end = end.getNext()
                if end == None:
                    return temp.getNext()
            nextBlock = end.getNext()
            self.reverseList(begin, end)
            previous.setNext(end)
            begin.setNext(nextBlock)
            previous = begin
        
def reverseList(self, start, end):
	alreadyReversed = start
	actual = start
	nextNode = start.getNext()
	while actual != end:
	    actual = nextNode
	    nextNode = nextNode.getNext()
	    actual.setNext(alreadyReversed)
	    alreadyReversed = actual
