from Coin import Coin
from MyExceptions.CannotConvertHeaviestCoinUpException import CannotConvertHeaviestCoinUpException
from MyExceptions.ConversionQuantityInvalidException import ConversionQuantityInvalidException
from MyExceptions.CoinNameDoesNotExistException import CoinNameDoesNotExistException

# ---------------------------------------
# Author: Peter Moyer & Nathaniel Markham
# Date Written: 17092020
# Date Modified: 18092020
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
    def __init__(self, platinumQuantity=0, goldQuantity=0, electrumQuantity=0, silverQuantity=0, copperQuantity=0):
        self.coins = [
            Coin("Copper", self.copperWeight, copperQuantity),
            Coin("Silver", self.silverWeight, silverQuantity),
            Coin("Electrum", self.electrumWeight, electrumQuantity),
            Coin("Gold", self.goldWeight, goldQuantity),
            Coin("Platinum", self.platinumWeight, platinumQuantity)
        ] # Make sure the elements are in order by weights, with the heaviest being the last element of the list

    def convertCoins(self, fromCoinName = None, toCoinName = None, fromCoinQuantity = None):
        # Save current coin quantities so that the conversion can be reversed if a mistake is made?
        fromCoin = None # To make sure fromCoin will have a value
        toCoin = None   # To make sure toCoin will have a value
        
        try:
            if fromCoinName != None:
                fromCoin = [x for x in self.coins if x.name == fromCoinName][0] # Find the element in the Coins list that matches the fromCoinName and store the whole Coin in fromCoin
        
            if toCoinName != None:
                toCoin = [x for x in self.coins if x.name == toCoinName][0] # Find the element in the Coins list that matches the toCoinName and store the whole Coin in toCoin
        
        except IndexError:
            raise CoinNameDoesNotExistException("The entered name is not a recognized Coin type.\n")

        if (fromCoin == None):
           for coin in self.coins:
                self.convertFromCoinToCoinByQuantity(coin, self.coins[self.coins.index(coin)+1], coin.quantity) # Convert as many as possible of each coin to the next heaviest coin, starting with the lightest coin
        else:
            if (toCoin == None) and (fromCoinQuantity == None):
                self.convertUpByQuantity(fromCoin, fromCoin.quantity) # Convert as many of the fromCoin to the next heaviest coin

            elif (toCoin == None) and (fromCoinQuantity != None):
                self.convertUpByQuantity(fromCoin, fromCoinQuantity) # Convert fromCoinQuantity of fromCoin to the next heaviest coin

            elif (toCoin != None) and (fromCoinQuantity == None):
                self.convertFromCoinToCoinByQuantity(fromCoin, toCoin, fromCoin.quantity) # Convert as many of fromCoin to toCoin as possible

            else:
                self.convertFromCoinToCoinByQuantity(fromCoin, toCoin, fromCoinQuantity) # Convert fromCoinQuantity of fromCoin to toCoin

    # Convert fromCoinQuantity number of fromCoin to the next heaviest coin
    def convertUpByQuantity(self, fromCoin, fromCoinQuantity):
        if fromCoin == self.coins[-1]: # If the coin to convertUp is the heaviest coin
            raise CannotConvertHeaviestCoinUpException("Cannot convert " + fromCoin.name + " to the next coin size up. It is the largest coin.\n")

        else:
            self.convertFromCoinToCoinByQuantity(fromCoin, self.coins[self.coins.index(fromCoin)+1], fromCoinQuantity)            

    # Convert fromCoinQuantity of fromCoin to toCoin
    def convertFromCoinToCoinByQuantity(self, fromCoin, toCoin, fromCoinQuantity):
        if fromCoinQuantity > fromCoin.quantity: # Check to make sure fromCoinQuantity does not exceed fromCoin.quantity
            raise ConversionQuantityInvalidException("Cannot convert that quantity of " + fromCoin.name + ". Value exceeds coin number or is negative.\n")
        
        else:
            temp = (fromCoinQuantity * fromCoin.weight) // toCoin.weight
            toCoin.quantity += temp
            fromCoin.quantity -= temp

    # Define a custom string representation for a Currency
    def __str__(self):
        return "\n".join(str(x) for x in self.coins)

# Could replace these with a pair of more general functions.
# One that takes a name, searches the list and finds the matching coin, and sets the quantity of coins to the specified amount.
# The other takes a name, searches the list and finds the matching coin, and returns the quantity of coins.
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
