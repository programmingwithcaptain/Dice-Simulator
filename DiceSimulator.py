# Python program to build a Dice Simulator Game

import random

roll_the_dice = True

while roll_the_dice:
    print(random.randint(1, 6))
    roll_the_dice_again = input("Do you want to roll the dice again (y/n): ")
    if roll_the_dice_again == "y":
        continue
    else:
        break
