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

    def __init__(self, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    @property
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, strength):
        self._strength = strength

    @property
    def dexterity(self):
        return self._dexterity

    @dexterity.setter
    def dexterity(self, dexterity):
        self._dexterity = dexterity
    
    @property
    def constitution(self):
        return self._constitution

    @constitution.setter
    def constitution(self, constitution):
        self._constitution = constitution
        
    @property
    def intelligence(self):
        return self._intelligence

    @intelligence.setter
    def intelligence(self, intelligence):
        self._intelligence = intelligence

    @property
    def wisdom(self):
        return self._wisdom

    @wisdom.setter
    def wisdom(self, wisdom):
        self._wisdom = wisdom
        
    @property
    def charisma(self):
        return self._charisma

    @charisma.setter
    def charisma(self, charisma):
        self._charisma = charisma

