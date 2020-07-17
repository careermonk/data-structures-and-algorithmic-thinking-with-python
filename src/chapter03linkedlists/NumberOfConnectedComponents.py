# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

class Solution(object):
    def numberOfConnectedComponents(self, head, S):
        s = set(S)
        current = head
        result = 0
        while current:
            if (current.data in s and
                    getattr(current.next, 'data', None) not in s):
                ans += 1
            current = current.next

        return result

