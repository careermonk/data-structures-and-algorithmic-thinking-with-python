# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

key = "Data Structure and Algorithmic Thinking with Python"
 
i = 0
while i < len(name_list) and name_list[i] != key:
    i += 1
 
if i < len(name_list):
    print("The name is at position", i)
else:
    print("The name was not in the list.")
