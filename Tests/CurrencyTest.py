
# ---------------------------------------
# Author: Peter Moyer & Nathaniel Markham
# Date Written: 17092020
# Date Modified: 18092020
# ---------------------------------------
# currency_test
# 
# Test each aspect of Currency
# ---------------------------------------
def currency_test():
    pass
# Order of Test Operations:
# Set the quantity for each coin to 101 and then get and display the information for each coin.
    # Test with fromCoinName = a coin not in the list. Don't care about other two.
    # Expected Result: fromCoinName was not in the list error

    # Test with toCoinName = a coin not in the list. Don't care about other two.
    # Expected Result: tomCoinName was not in the list error

    # Test with fromCoinName = heaviest coin. Set others to None
    # Expected Result: Cannot convert heaviest coin up error.

    # Test with fromCoinName = a coin in the list and fromCoinQuantity = < 0 or > than that coin's quantity (101 should work in this case)
    # Expected Result: Quantity exceeds the number of coins or is negative.

    # Test with fromCoinName = Gold and toCoinName = Gold, fromCoinQuantity = None.
    # Expected Result: 101C, 101S, 101E, 101G, 101P

    # Test with None values for fromCoinName and toCoinName, don't care about fromCoinQuantity.
    # Expected Result: 1C, 2S, 1E, 52G, 102P

# Set the quantity for each coin to 101 and then get and display the information for each coin.
    # Test with fromCoinName = Gold, toCoinName = Silver, fromCoinQuantity = 1
    # Expected Result: 101C, 201S, 101E, 100G, 101P

    # Test with fromCoinName = Silver, toCoinName = Gold, fromCoinQuantity = 1
    # Expected Result: 101C, 201S, 101E, 100G, 101P

    # Test with fromCoinName = Silver, toCoinName = None, fromCoinQuantity = 100
    # Expected Result: 101C, 101S, 101E, 101G, 101P

    # Test with fromCoinName = Gold, toCoinName and fromCoinQuantity = None
    # Expected Result: 101C, 101S, 101E, 1G, 102P

    # Test with fromCoinName = Platinum, toCoinName = Gold, and fromCoinQuantity = None
    # Expected Result: 101C, 101S, 101E, 1201G, 0P

    # Test with fromCoinName = None and toCoinName = Gold. Don't care about fromCoinQuantity.
    # Expected Result: 1C, 2S, 1E, 52G, 102P
