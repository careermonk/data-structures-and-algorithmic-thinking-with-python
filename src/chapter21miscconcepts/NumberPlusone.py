# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

#!/usr/bin/env python
'''
Given a number represented as an array of digits, plus one to the number.
'''
from __future__ import division
import random

def plus_one(digits):
    print digits, '+ 1 =',
    carry = 1
    for i in reversed(xrange(len(digits))):
        x = digits[i]
        carry, x = divmod(x + carry, 10)
        digits[i] = x
    if carry > 0: digits.insert(0, carry)
    print digits
    return digits

if __name__ == '__main__':
    plus_one([1, 2, 3, 4])
    plus_one([1, 9, 9])
    plus_one([9, 9, 9])
    plus_one([0])
