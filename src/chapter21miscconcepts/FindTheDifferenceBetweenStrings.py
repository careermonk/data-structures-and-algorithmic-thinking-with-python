# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def findTheDifference1(s, t):
    for i in range(len(t)):
        found = False
        for j in range(len(s)):
            if s[j] == t[i]:
                found = True
        if found == False:
            return t[i]

def findTheDifference2(s, t):
    s = sorted(s)
    t = sorted(t)
    for i in range(len(t)):
        if (i == len(t)-1) or (s[i] != t[i]):
            return t[i]

def findTheDifference3(s, t):
    result = 0
    for i in range(len(t)):
        result = result + ord(t[i])
    for i in range(len(s)):
        result = result - ord(s[i])
    return chr(result)

def findTheDifference4(s, t):
    hashTable = {}
    for i in range(len(s)):
        hashTable[s[i]] = True
    for i in range(len(t)):
        if hashTable.get(t[i]) is None:
            return t[i]

def findTheDifference5(s, t):
    c = 0
    for i in range(len(s)):
        c = c ^ ord(s[i])
    for i in range(len(t)):
        c = c ^ ord(t[i])
    return chr(c)
print (findTheDifference1("abcd","baedc"))
print (findTheDifference2("abcd","baedc"))
print (findTheDifference3("abcd","baedc"))
print (findTheDifference4("abcd","baedc"))
print (findTheDifference5("abcd","baedc"))
