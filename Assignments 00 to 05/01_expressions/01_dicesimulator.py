#Ans of Q1 in expressions

#Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random

def roll_dice():

    die1 = int(random.randint(1,6))
    die2 = int(random.randint(1,6))
    total: int = die1 + die2
    print("Total of two dice:", total)


for i in range(3):
     print("Roll", i + 1)

     roll_dice()



