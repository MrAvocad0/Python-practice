from cs50 import get_float
import math


def main():
    # Multiply the change into integer values *100
    # Coin counter
    # Change into an array to call from
    change = get_pos()
    cents = round(change * 100)
    coins = 0
    current_coins = 0;
    change_amounts = [25, 10, 5, 1]
    
    # Iterate from largest value of change to smallest
    # Divide biggest change value into change
    # Update coin counter with how many times that coin can go into change
    # Restate the value of the remaining change.
    for i in range(len(change_amounts)):
        if cents > 0:
            current_coins = math.floor(cents / change_amounts[i])
            coins = coins + current_coins
            cents = cents - (current_coins * change_amounts[i])
    print(coins)

def get_pos():
    # Getting floating change value
    # Make sure its positive
    while True:
        change = get_float("What is changed owed?\n")
        if change > 0:
            break
    return change
main()