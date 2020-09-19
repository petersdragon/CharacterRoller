# ---------------------------------------
# Author: Peter Moyer
# Date Written: 17092020
# Date Modified: 18092020
# ---------------------------------------
# Coin
# 
# A coin knows its name, weight, and how
# many of that type of coin there are.
# ---------------------------------------
class Coin():

    def __init__(self, name, weight, quantity=0):
        self.name = name
        self.weight = weight
        self.quantity = quantity

    # Define a custom string representation for a Coin
    def __str__(self):
        return self.quantity + " " + self.name

    @property
    def name(self):
        return self._name # Get the value of name

    @name.setter
    def name(self, name):
        self._name = name # Set the value of name

    @property
    def weight(self):
        return self._weight # Get the value of weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight # Set the value of weight

    @property
    def quantity(self):
        return self._quantity # Get the value of quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity # Set the value of quantity

