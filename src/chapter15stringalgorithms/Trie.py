# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import sys

class TrieNode :

    def __init__(self) :
       self.word = None
       self.letter = [None for i in range(26)]

class Trie :
    def __init__(self):
       self.root = TrieNode()

    def add(self, word):
        self.recAdd(self.root, word, 0, len(word))

    def recAdd(self, r, word, place, length):
        if place == length :
             r.word = word
        else: 
             i = ord(word[place]) - 65
             if r.letter[i] == None:
                  r.letter[i] = TrieNode()
             self.recAdd(r.letter[i], word, place + 1, length)

    def search(self, word):
        self.count = 0
        return [self.recSearch(self.root, word, 0, len(word)), self.count]

    def recSearch(self, r, word, place, length): 
      if  place == length: 
          if r.word == None:
              return None
          else:
              return r
      else :
           i = ord(word[place]) - 65
           if r.letter[i] == None:
                self.count = self.count + 1
                return None
           else: 
                self.count = self.count + 1
                return self.recSearch(r.letter[i], word, place + 1, length)
      

def tester():
    infile = open(sys.argv[1], 'r')
    f = infile.read()
    x = f.split()
    for i in range(len(x)): 
        x[i] = x[i].upper()
    trie = Trie()
    for i in range(len(x)):
        trie.add(x[i])
    w = raw_input("Enter a word ")
    w = w.upper()
    while w != "Q":
         if w != 'Q': 
           print w
           [t, count] = trie.search(w)
           if t == None:
              print "word not in dictionary", "count = ", count
           else:
              print t.word, " found", " count = ", count
           w = raw_input("Enter a word ")
           w = w.upper()
     

if __name__ == '__main__':
    tester()


 
