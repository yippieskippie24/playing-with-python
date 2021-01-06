#!/usr/bin/env python3
#written by Tyler M Johnson
#https://github.com/yippieskippie24/playing-with-python

import random


#ask what size die is needed
print ("4")
print ("6")
print ("8")
print ("10")
print ("12")
print ("20")
print ("100")

die_size = int(input("What Die should be rolled? "))
die_count = int(input("How many dice should be rolled? "))


def rollDice():
    #Variables
    min = 1
    max = die_size
    x = int
    roll_again = "yes"
    die_array = []
    total = int(0)
    

    print ("Rolling the dices...")
    print ("The values are....")
    for x in range(die_count):
        single_die = int(random.randint(min, max))
        print (single_die)
        die_array.append(single_die)
    for x in die_array:
        total += x
    print("Total of dice rolled: " )
    print(total)
    
rollDice()
