# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail                   : info@careermonk.com 
# Creation Date            : 2014-01-10 06:15:46 
# Last modification        : 2008-10-31 
#               by        : Narasimha Karumanchi 
# Book Title            : Data Structures And Algorithmic Thinking With Python
# Warranty                 : This software is provided "as is" without any 
#                    warranty; without even the implied warranty of 
#                     merchantability or fitness for a particular purpose. 

def InterpolationSearch(numbersList, value):
    low = 0
    high = len(numbersList) - 1
    while numbersList[low] <= value and numbersList[high] >= value:
        mid = (low + ((value - numbersList[low]) * (high - low))
               / (numbersList[high] - numbersList[low]))
        if numbersList[mid] < value:
            low = mid + 1
        elif numbersList[mid] > value:
            high = mid - 1
        else:
            return mid
    if numbersList[low] == value:
        return low
    return None

A = [-30,-16,-9,3,10,11,18,22,54,84,105]
print InterpolationSearch(A, -9)
