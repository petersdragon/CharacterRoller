# ---------------------------------------
# Author: Peter Moyer
# Date Written: 18092020
# Date Modified: 18092020
# ---------------------------------------
# ConversionQuantityInvalidQuantity
# 
# For when there are not enough coins to
# complete the requested conversion
# ---------------------------------------

class ConversionQuantityInvalidException(Exception):
    def __init__(self, message):
        self.message = message
