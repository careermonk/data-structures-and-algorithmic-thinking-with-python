# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def RobinKarp(text, pattern):
        if pattern == None or text == None:
                return -1
        if pattern == "" or text == "":
                return -1

        if len(pattern) > len(text):
                return -1

        hashText = Hash(text, len(pattern))
        hashPattern = Hash(pattern, len(pattern))
        hashPattern.update()

        for i in range(len(text) - len(pattern) + 1):
            if hashText.hashedValue() == hashPattern.hashedValue():
                if hashText.text() == pattern:
                    return i
            hashText.update()

        return -1

class Hash:
        def __init__(self, text, size):
                self.str = text
                self.hash = 0

                for i in xrange(0, size):
                        self.hash += ord(self.str[i])

                self.init = 0
                self.end = size

        def update(self):
                if self.end <= len(self.str) - 1:
                        self.hash -= ord(self.str[self.init])
                        self.hash += ord(self.str[self.end])
                        self.init += 1
                        self.end += 1

        def hashedValue(self):
                return self.hash

        def text(self):
                return self.str[self.init:self.end]		
                
print RobinKarp("3141592653589793", "26")                
