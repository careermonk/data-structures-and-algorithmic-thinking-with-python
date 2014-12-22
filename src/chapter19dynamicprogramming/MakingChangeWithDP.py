def MakingChange(coins, change, minimumCoins, coinsUsed):
   for cents in range(change + 1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coins if c <= cents]:
            if minimumCoins[cents - j] + 1 < coinCount:
               coinCount = minimumCoins[cents - j] + 1
               newCoin = j
      minimumCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minimumCoins[change]

def printingCoins(coinsUsed, change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amountToGetChange = 63
    coins = [1, 5, 10, 21, 25]
    coinsUsed = [0] * (amountToGetChange + 1)
    coinCount = [0] * (amountToGetChange + 1)

    print("Making change for", amountToGetChange, "requires")
    print(MakingChange(coins, amountToGetChange, coinCount, coinsUsed), "coins")
    print("They are:")
    printingCoins(coinsUsed, amountToGetChange)
    print("The used list is as follows:")
    print(coinsUsed)

main()
