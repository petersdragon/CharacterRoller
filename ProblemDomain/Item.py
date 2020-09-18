# ---------------------------------------
# Author: Peter Moyer
# Date Written: 17092020
# Date Modified: 17092020
# ---------------------------------------
# Item
# 
# Describes an item. It could be a
# weapon, gemstone, or anything else.
# ---------------------------------------
class Item():

    def __init__(self, name):
        self.name = name
        # Open the appropriate race file based on the name for all the rest of the information
        # From the file:
        # self.description = description from file
        # self.price = price from file
        # self.weight = weight from file

    @property
    def name(self):
        return self._name # Get the value of name

    @name.setter
    def name(self, name):
        self._name = name # Set the value of name

    @property
    def description(self):
        return self._description # Get the value of description

    @description.setter
    def description(self, description):
        self._description = description # Set the value of description

    @property
    def weight(self):
        return self._weight # Get the value of weight

    @weight.setter
    def weight(self, weight):
        self._weight = weight # Set the value of weight

    @property
    def price(self):
        return self._price # Get the value of price

    @price.setter
    def price(self, price):
        self._price = price # Set the value of price





