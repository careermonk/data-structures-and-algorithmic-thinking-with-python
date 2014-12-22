# Copyright (c) Dec 22, 2014 CareerMonk Publications and others.
# E-Mail           		: info@careermonk.com 
# Creation Date    		: 2014-01-10 06:15:46 
# Last modification		: 2008-10-31 
#               by		: Narasimha Karumanchi 
# Book Title			: Data Structures And Algorithmic Thinking With Python
# Warranty         		: This software is provided "as is" without any 
# 				   warranty; without even the implied warranty of 
# 				    merchantability or fitness for a particular purpose. 

def calculateProfitWhenBuyingNow(A, index):
    buyingPrice = A[index]
    maxProfit = 0
    sellAt = index
    for i in range(index + 1, len(A)):
        sellingPrice = A[i]
        profit = sellingPrice - buyingPrice
        if profit > maxProfit:
            maxProfit = profit
            sellAt = i

    return maxProfit, sellAt
    
# check all possible buying times
def StockStrategyBruteForce(A):
    maxProfit = None
    buy = None
    sell = None
    
    for index, item in enumerate(A):
        profit, sellAt = calculateProfitWhenBuyingNow(A, index)
        if (maxProfit is None) or (profit > maxProfit):
            maxProfit = profit
            buy = index
            sell = sellAt
            
    return maxProfit, buy, sell
