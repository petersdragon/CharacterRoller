# ---------------------------------------
# Author: Peter Moyer
# Date Written: 17092020
# Date Modified: 17092020
# ---------------------------------------
# Attributes
# 
# Store the values for the common
# Attributes in D&D. Strength, 
# Dexterity, Constitution, Intelligence,
# Wisdom, and Charisma.
# ---------------------------------------

class Attributes():

    # Initialize the instance of the Attributes object with 0's or with input
    def __init__(self, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    @property
    def strength(self):
        return self._strength # Get the value of Strength

    @strength.setter
    def strength(self, strength):
        self._strength = strength # Set the value of Strength

    @property
    def dexterity(self):
        return self._dexterity # Get the value of Dexterity

    @dexterity.setter
    def dexterity(self, dexterity):
        self._dexterity = dexterity # Set the value of Dexterity
    
    @property
    def constitution(self):
        return self._constitution # Get the value of Constitution

    @constitution.setter
    def constitution(self, constitution):
        self._constitution = constitution # Set the value of Constitution
        
    @property
    def intelligence(self):
        return self._intelligence # Get the value of Intelligence

    @intelligence.setter
    def intelligence(self, intelligence):
        self._intelligence = intelligence # Set the value of Intelligence

    @property
    def wisdom(self):
        return self._wisdom # Get the value of Wisdom

    @wisdom.setter
    def wisdom(self, wisdom):
        self._wisdom = wisdom # Set the value of Wisdom
        
    @property
    def charisma(self):
        return self._charisma # Get the value of Charisma

    @charisma.setter
    def charisma(self, charisma):
        self._charisma = charisma # Set the value of Charisma

