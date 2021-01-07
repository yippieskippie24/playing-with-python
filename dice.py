#!/usr/bin/env python3
# written by Tyler M Johnson
# https://github.com/yippieskippie24/playing-with-python

import random
import time

# ask what size die is needed
print("Typical Dice to roll: 4, 6, 8, 12, 20, 100")

die_size: int = int(input("What Die should be rolled? "))
die_count: int = int(input("How many dice should be rolled? "))


def roll_dice():
    # Variables
    die_min = 1
    die_max = die_size
    die_array = []
    total = int(0)
    separator = ", "

    print("Rolling the dices...")
    time.sleep(1)
    print("The values are....")
    for roll in range(die_count):
        single_die = int(random.randint(die_min, die_max))
        die_array.append(single_die)
    print(separator.join(map(str, die_array)))
    for roll in die_array:
        total += roll
    print("Total of dice rolled: %d" % total)


roll_dice()
