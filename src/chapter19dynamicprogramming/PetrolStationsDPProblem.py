# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def canCompleteTour(self, petrol, cost):
	minVal = float("inf")
	minPos = -1
	petrolTillNow = 0
	for i in range(0, len(petrol)):
	    petrolTillNow += petrol[i] - cost[i]
	    if petrolTillNow < minVal:
		minVal = petrolTillNow
		minPos = i
	if petrolTillNow >= 0:
	    return (minPos + 1) % len(petrol)
	return -1
