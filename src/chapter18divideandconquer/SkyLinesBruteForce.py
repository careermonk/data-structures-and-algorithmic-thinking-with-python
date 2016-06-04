# Copyright (c) Feb 22, 2016 CareerMonk Publications and others.
# E-Mail                   : info@careermonk.com 
# Creation Date            : 2016-02-22 06:15:46 
# Last modification        : 2008-10-31 
#               by        : Narasimha Karumanchi 
# Book Title            : Data Structures And Algorithmic Thinking With Python
# Warranty                 : This software is provided "as is" without any 
#                    warranty; without even the implied warranty of 
#                     merchantability or fitness for a particular purpose. 


def SkyLineBruteForce():
    auxHeights = [0]*1000
    rightMostBuildingRi=0
    p = raw_input("Enter three values:  ") # raw_input() function
    inputValues = p.split()  
    inputCount = len(inputValues)
    while inputCount==3:
        left = int(inputValues[0])
        h = int(inputValues[1])
        right = int(inputValues[2])
        for i in range(left,right-1):
            if(auxHeights[i]<h):
                auxHeights[i]=h;    
        if(rightMostBuildingRi<right):
                    rightMostBuildingRi=right
        
        p = raw_input("Enter three values:  ") # raw_input() function
        inputValues = p.split()  
        inputCount = len(inputValues)

    prev = 0
    for i in range(1,rightMostBuildingRi-1):
        if prev!=auxHeights[i]:
            print i, " ", auxHeights[i]
        prev=auxHeights[i]
    print rightMostBuildingRi, " ", auxHeights[rightMostBuildingRi]

SkyLineBruteForce()