
from Coin import Coin

# ---------------------------------------
# Author: Peter Moyer & Nathaniel Markham
# Date Written: 17092020
# Date Modified: 17092020
# ---------------------------------------
# Currency
# 
# Store the number of coins of each type
# commonly available in D&D. Platinum, 
# Gold, Electrum, Silver, and Copper.
# ---------------------------------------
class Currency():

    copperWeight = 1        # Reference weight
    silverWeight = 10       # Number of copper in a silver
    electrumWeight = 50     # Number of copper in a electrum
    goldWeight = 100        # Number of copper in a gold
    platinumWeight = 1000   # Number of copper in a platinum

    # Initialize the instance of the Currency object with 0's or with input
    def __init__(self, platinum=0, gold=0, electrum=0, silver=0, copper=0):
        self.coins = [
            Coin("Copper", self.copperWeight, copper),
            Coin("Silver", self.silverWeight, silver),
            Coin("Electrum", self.electrumWeight, electrum),
            Coin("Gold", self.goldWeight, gold),
            Coin("Platinum", self.platinumWeight, platinum)
        ] # Make sure the elements are in order by weights, with the heaviest being the last element of the list

    # Converts each coin to the highest size it can be
    def convertToHighest(self):
        for coin in self.coins:
            self.convertUp(coin)

    # Convert as many of the fromCoin to the next coin up
    def convertUp(self, fromCoin):
        if fromCoin != self.coins[-1]: # Make sure it is not the heaviest coin being converted up
            self.convertFromCoinToCoin(fromCoin, self.coins[self.coins.index(fromCoin)+1])

        else:
            # Cannot convert highest weighted coin up
            pass

    # Convert fromCoinQuantity number of fromCoin to the next highest coin size
    def convertUpByQuantity(self, fromCoin, fromCoinQuantity):
        # Check that Platinum is not being converted up.
        pass

    # Convert as many of fromCoin to toCoin as possible
    def convertFromCoinToCoin(self, fromCoin, toCoin):
        temp = (fromCoin.quantity * fromCoin.weight) // toCoin.weight
        toCoin.quantity += temp
        fromCoin.quantity -= temp*fromCoin.weight
    

    def convertFromCoinToCoinByQuantity(self, fromCoin, toCoin, fromCoinQuantity):
        # Convert fromCoinQuantity of fromCoin to toCoin
        pass

    def convertCoins(self, fromCoin = None, toCoin = None, fromCoinQuantity = None):
        # Save current coin quantities so that the conversion can be reversed if a mistake is made?
        if (fromCoin == None):
            self.convertToHighest()

        else:
            if (toCoin == None) and (fromCoinQuantity == None):
                self.convertUp(fromCoin)

            elif (toCoin == None) and (fromCoinQuantity != None):
                self.convertUpByQuantity(fromCoin, fromCoinQuantity)

            elif (toCoin != None) and (fromCoinQuantity == None):
                self.convertFromCoinToCoin(fromCoin, toCoin)

            else:
                self.convertFromCoinToCoinByQuantity(fromCoin, toCoin, fromCoinQuantity)

        # Display message about which path was executed

    @property
    def platinum(self):
        return self._platinum # Get number of Platinum coins

    @platinum.setter
    def platinum(self, platinum):
        self._platinum = platinum # Set number of Platinum coins
    
    @property
    def gold(self):
        return self._gold # Get number of Gold coins

    @gold.setter
    def gold(self, gold):
        self._gold = gold # Set number of Gold coins

    @property
    def electrum(self):
        return self._electrum # Get number of Electrum coins

    @electrum.setter
    def electrum(self, electrum):
        self._electrum = electrum  # Set number of Electrum coins
    
    @property
    def silver(self):
        return self._silver # Get number of Silver coins

    @silver.setter
    def silver(self, silver):
        self._silver = silver # Set number of Silver coins
        
    @property
    def copper(self):
        return self._copper # Get number of Copper coins

    @copper.setter
    def copper(self, copper):
        self._copper = copper # Set number of Copper coins

