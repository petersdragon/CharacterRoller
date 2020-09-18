# ---------------------------------------
# Author: Peter Moyer
# Date Written: 17092020
# Date Modified: 17092020
# ---------------------------------------
# Race
# 
# Reads the information regarding the 
# character's Race from the appropriate
# file based on the race name, then
# assigns or stores the race benefits and
# modifications
# ---------------------------------------
class Race():

    # Set the name of the race, 
    # a description for the race, 
    # the bonus attributes for the race, 
    # the languages governed by the race,
    # and the race-specific features.
    def __init__(self, name):
        self.name = name
        # Open the appropriate race file based on the name for all the rest of the information
        # From the file:
            # Set the race's description
            # Adjust the Character's attributes based on the bonus attributes
            # Add the race languages to the Character's Languages list.
            # Speed and their types
            # Vision types/distance
            # Spells (if applicable)
            # Add the racial feature(s) to the Character's Feat(?) list
        
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

