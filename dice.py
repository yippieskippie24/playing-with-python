import random


#ask what size die is needed
print ("4")
print ("6")
print ("8")
print ("10")
print ("12")
print ("20")
print ("100")

die_size = input("What Die should be rolled? ")
die_count = input("How many dice should be rolled? ")

min = 1
max = die_size
x = int
roll_again = "yes"
single_die = ""
total = ""
while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    for x in range(die_count):
        single_die = random.randint(min, max)
        print single_die
        

    roll_again = raw_input("Roll the dices again? ")