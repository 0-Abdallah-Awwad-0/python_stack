# Assignment: Functions Intermediate I

import random


def randInt(min=0, max=100):
    # Bonus edge case:
    # if min is bigger than max, return False
    if min > max:
        return False

    # random.random() gives number from 0 to 1
    # max - min gives the range
    # + min moves the number into the correct range
    num = random.random() * (max - min) + min

    # round changes it into an integer
    return round(num)


print(randInt())                  # random number between 0 and 100
print(randInt(max=50))            # random number between 0 and 50
print(randInt(min=50))            # random number between 50 and 100
print(randInt(min=50, max=500))   # random number between 50 and 500

# Bonus tests
print(randInt(min=500, max=50))   # False