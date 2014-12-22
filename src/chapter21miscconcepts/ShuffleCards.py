# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

import random
def shuffle(cards):
    max = len(cards) - 1
    while max != 0:
        r = random.randint(0, max)
        cards[r], cards[max] = cards[max], cards[r]
        max = max - 1
    return cards

actual = range(1, 53)
shuffle(actual)
