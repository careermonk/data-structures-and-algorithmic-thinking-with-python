# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail                   : info@careermonk.com 
# Creation Date            : 2014-01-10 06:15:46 
# Last modification        : 2008-10-31 
#               by        : Narasimha Karumanchi 
# Book Title            : Data Structures And Algorithmic Thinking With Python
# Warranty                 : This software is provided "as is" without any 
#                    warranty; without even the implied warranty of 
#                     merchantability or fitness for a particular purpose. 



def counting_number_of_ones_in_1_to_N(n):
    count = 0
    for i in range(1, n+1):
        j = i;
        while(j):
            count += 1
            j &= j - 1
    print count

n = 2
counting_number_of_ones_in_1_to_N(n)
n = 5
counting_number_of_ones_in_1_to_N(n)
n = 7
counting_number_of_ones_in_1_to_N(n)
n = 8
counting_number_of_ones_in_1_to_N(n)
