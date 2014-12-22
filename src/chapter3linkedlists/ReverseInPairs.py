# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithms Made In Java
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

  def reverseInPairs(self) :
    temp = self.head
    while None != temp and None != temp.getNext():
      self.swapData(temp, temp.getNext())
      temp = temp.getNext().getNext()
 
  def swapData(self, a, b):
    tmp = a.getData()
    a.setData(b.getData())
    b.setData(tmp)
