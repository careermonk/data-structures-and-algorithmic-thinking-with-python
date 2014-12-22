# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class Stack:
    def __init__(self):
        self.items = []
         
    # method for pushing an item on a stack
    def push(self, item):
        self.items.append(item)
         
    # method for popping an item from a stack
    def pop(self):
        return self.items.pop()
     
    # method to check whether the stack is empty or not
    def isEmpty(self):
        return (self.items == [])
     
    # method to get the top of the stack
    def peek(self):
        return self.items[-1]
     
    def __str__(self):
        return str(self.items)
     
def matches(top, symbol):
    openingSymbols = "({["
    closingSymbols = ")}]"
     
    return openingSymbols.index(top) == closingSymbols.index(symbol)
 
 
def checkSymbolBalance(input):
    symbolstack = Stack()
    balanced = 0
    for symbols in input:
        if symbols in ["(", "{", "["]:
            symbolstack.push(symbols)
        else:
            if symbolstack.isEmpty():
                balanced = 0
            else:
                topSymbol = symbolstack.pop()
                if not matches(topSymbol, symbols):
                    balanced = 0
                else:
                    balanced = 1
                     
    return balanced
 
print checkSymbolBalance("([)]") 
'''Output: 0'''
 
print checkSymbolBalance("{{([][])}()}") 
'''Output: 1'''
