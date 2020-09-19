# ---------------------------------------
# Author: Peter Moyer
# Date Written: 18092020
# Date Modified: 18092020
# ---------------------------------------
# CoinNameDoesNotExistException
# 
# For when a coin's name is not found in
# the list of accepted coins.
# ---------------------------------------

class CoinNameDoesNotExistException(ValueError):
    def __init__(self, message):
        self.message = message
