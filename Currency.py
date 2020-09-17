# ---------------------------------------
# Author: Peter Moyer
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

    # Initialize the instance of the Currency object with 0's or with input
    def __init__(self, platinum=0, gold=0, electrum=0, silver=0, copper=0):
        self.platinum = platinum
        self.gold = gold
        self.electrum = electrum
        self.silver = silver
        self.copper = copper

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

