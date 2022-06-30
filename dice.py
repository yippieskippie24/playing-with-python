#!/usr/bin/env python3
# Written by Tyler M Johnson
# https://github.com/yippieskippie24/playing-with-python

import random
import time

# ask what size die is needed
print("Typical Dice to roll: 4, 6, 8, 12, 20, 100")

def roll_dice():
    # Variables
    die_min = 1
    die_max = int(input("What Die should be rolled? "))
    die_array = []
    total = int(0)
    separator = ", "


    for i in range(int(input("How many dice should be rolled? "))):
        die_array.append(int(random.randint(die_min, die_max)))
    print("Rolling the dices...")
    time.sleep(1)
    print("The values are....")
    print(separator.join(map(str, die_array)))
    for i in die_array:
        total += i
    print("Total of dice rolled: %d" % total)
    print("")

def roll_again():
    answer = str(input("Roll dice again?  y or n: "))
    if answer == "y":
        roll_dice()
    elif answer == "n":
        exit()
    else :
        print("Please enter y or n")
        roll_again()

roll_dice()
roll_again()