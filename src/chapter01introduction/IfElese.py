# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

# O(1)
def simple_if_condition(n):
    i = n
    if i == 0: 
        i = i + 1
    print i
        
# O(1)
def if_else_condition(n):
    i = n
    if i == 0: 
        i = i + 1
    elif i == 1:
        i += 2    
    print i  
    
# O(n)
def if_else_condition2(n):
    i = n
    if i > 0: 
        for j in range(1,n):
            print j
    elif i < 0:
        i += 2    
    print i   
    
# O(n^2): Note that if testFunction is executed always
def if_else_condition3(n):
    i = n
    if test_function(n) > 0: 
        for j in range(1,n):
            print j
    elif i < 0:
        i += 2    
    print i   

# O(n)    
def test_function(n):
    for j in range(1,n):
            print j           