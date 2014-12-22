# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class SmartStack:
    def __init__(self):
        self.stack = []
        self.min = []
    def stack_push(self, x):
	self.stack.append(x)
	if not self.min or x <= self.stack_min():
		self.min.append(x)
            
    def stack_pop(self):
        x = self.stack.pop()
        if x == self.stack_min():
            self.min.pop()
        return x

    def stack_min(self):
        return self.min[-1]

def main():
    print "Push elements to the stack"
    list = range(10)
    stack = SmartStack()
    for i in list:
        stack.stack_push(i)
    print "Print stack and stack minimum"
    print stack.stack
    print stack.stack_min()
    print "Push -1 to stack, print stack and stack minimum"
    stack.stack_push(-1)
    print stack.stack
    print stack.stack_min()
    print "Pop from stack, print stack and stack minimum"
    print stack.stack_pop()
    print stack.stack
    print stack.stack_min()

if __name__ == "__main__":
    main()
