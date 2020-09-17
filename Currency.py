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

    def __init__(self, platinum=0, gold=0, electrum=0, silver=0, copper=0):
        self.platinum = platinum
        self.gold = gold
        self.electrum = electrum
        self.silver = silver
        self.copper = copper

    @property
    def platinum(self):
        return self._platinum

    @platinum.setter
    def platinum(self, platinum):
        self._platinum = platinum
    
    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, gold):
        self._gold = gold

    @property
    def electrum(self):
        return self._electrum

    @electrum.setter
    def electrum(self, electrum):
        self._electrum = electrum
    
    @property
    def silver(self):
        return self._silver

    @silver.setter
    def silver(self, silver):
        self._silver = silver
        
    @property
    def copper(self):
        return self._copper

    @copper.setter
    def copper(self, copper):
        self._copper = copper

