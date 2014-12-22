# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def nthNodeFromEnd(self, n):
    if 0 > n:
      return None
 
    # count k units from the self.head.
    temp = self.head
    count = 0
    while count < n and None != temp:
      temp = temp.next
      count += 1
 
    # if the LinkedList does not contain k elements, return None
    if count < n or None == temp:
      return None
 
    # keeping tab on the nth element from temp, slide temp until
    # temp equals self.tail. Then return the nth element.
    nth = self.head
    while None != temp.next:
      temp = temp.next
      nth = nth.next
 
    return nth
