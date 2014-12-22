# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class Stack(object):
    def __init__(self, items=[]):
        self.stack = items

    def is_empty(self):
        return not self.stack

    def pop(self):
        return self.stack.pop()

    def push(self, data):
        self.stack.append(data)

    def __repr__(self):
        return "Stack {0}".format(self.stack)

def reverseStack(stack):
    def reverseStackRecursive(stack, newStack=Stack()):
        if not stack.is_empty():
            newStack.push(stack.pop())
            reverseStackRecursive(stack, newStack)
        return newStack
    return reverseStackRecursive(stack)


s = Stack(range(10))
print s
print reverseStack(s)
