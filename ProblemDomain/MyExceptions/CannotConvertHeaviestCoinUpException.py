# ---------------------------------------
# Author: Peter Moyer
# Date Written: 18092020
# Date Modified: 18092020
# ---------------------------------------
# CannotConvertHeaviestCoinUpException
# 
# For when a coin is converted higher
# than the maximum weighted coin 
# available.
# ---------------------------------------

class CannotConvertHeaviestCoinUpException(Exception):
    def __init__(self, message):
        self.message = message
