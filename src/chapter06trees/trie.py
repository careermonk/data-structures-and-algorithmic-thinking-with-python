# Copyright (c) Feb 26, 2021 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2021-02-26 06:15:46 
# Last modification		: 2021-02-26 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isLeaf = False
    
    def insert(self, word):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.isLeaf = True
        
    def search(self, word):
        current = self
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.isLeaf
    
    def wordsWithPrefix(self, prefix):
        current = self
        result = []
        
        def printer(current, path, result):
            if current.isLeaf == True:
                result.append(path)
                
            for child in current.children:
                printer(current.children[child], path + child, result)
        
        for char in prefix:
            if char not in current.children:
                return result
            current = current.children[char]
            
        printer(current, prefix, result)
        return result
    
    def printWords(self):
        current = self
        result = []
        def printer(current, path, result):
            if current.isLeaf == True:
                result.append(path)
                
            for child in current.children:
                printer(current.children[child], path + child, result)
        
        printer(current, "", result)
        return result
    
    
words = "banana bananas bandana band apple all beast"

root = TrieNode()
for word in words.split(" "):
    root.insert(word)

for word in words.split(" "):
    print(root.search(word))
    
print(root.printWords())

print(root.wordsWithPrefix("a"))
