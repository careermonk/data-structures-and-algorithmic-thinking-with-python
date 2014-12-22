# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 


class Node(object):
    def __init__(self):
        self.children = {}  # contains a map with child characters as keys and their Node as values

class Trie(object):

    def __init__(self):
        self.root = Node()
        self.root.data = "/" 
	
    def addWord(self, word):
        currentNode = self.root
        i = 0
        # print "adding word '"+ word+"' to trie "
        for c in word:
            # print "adding character " + c
            try:
                currentNode = currentNode.children[c]
		# print "character "+c + " exists"
            except:
                self.createSubTree(word[i:len(word)], currentNode)
                break
            i = i + 1
                
            
    def addCharacter(self, c, children):
        i = 0;
        for existingc in children:
            if existingc > c:
                children.insert(i, c)
                break
            i = i + 1
           
 
    def createSubTree(self, word, node):
        # print "creating subtree for " + word
        currentNode = node
        for c in word:
            currentNode.children[c] = Node()
            currentNode.children[c].data = c
            currentNode.children[c].parent = currentNode
            currentNode = currentNode.children[c]
                         
    def printTree(self):
	nodestack = [self.root]
        while len(nodestack) != 0:
		currentNode = nodestack.pop()
		values = ""
        	for n in currentNode.children:
			temp = currentNode.children[n]
        		values += " " + temp.data
			nodestack.append(temp)

    def getWordList(self, startingCharacters):
	    startNode = self.root
	    for c in startingCharacters:
		    try:
			 startNode = startNode.children[c]
		    except:
	    		return []
	    nodestack = []
	    for child in startNode.children:
	    	nodestack.append(startNode.children[child])
	    words = []
	    currentWord = ""
	    while len(nodestack) != 0:
		    currentNode = nodestack.pop()
		    currentWord += currentNode.data
		    if len (currentNode.children) == 0:
			words.append(startingCharacters + currentWord)
			currentWord = ""

		    for n in currentNode.children:
			    temp = currentNode.children[n]
			    nodestack.append(temp)
	    return words
