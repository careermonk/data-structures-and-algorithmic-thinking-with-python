# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

myString = "We want to get the counts for each letter in this sentence"
counts = {}

for letter in myString:
    counts[letter] = counts.get(letter, 0) + 1
print counts

sortedKeys = sorted(counts.keys(), key=lambda x: counts[x])
for k in sortedKeys:
    print k , "-->" , counts[k]
