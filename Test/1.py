from random import randrange as rd
from time import sleep as sl
import random

sl(rd(1, 2))

print("Enter a number between 1 and 10000")
sl(rd(1, 2))

print("Entering a word will give an error")

b = 0
UI = input("Input: ")
UI = int(UI)
UI_Filter = None

if UI > 10000:
    print("Too high")
elif UI < 1:
    print("Too low")
else:
    print("Number accepted")
    UI_Filter = True

while UI_Filter:
    RandomNumber = rd(1, 100000)
    print(f"\033[94m{RandomNumber}\033[0m")
    b = b + 1
    if RandomNumber == UI:
        sl(2.568)
        print("\033[92mCorrect\033[0m")
        sl(1)
        RNstr = str(RandomNumber)
        print("IT TOOK")
        for digit in RNstr:
            color_code = random.randint(36, 37)  # Generate a random color code between 31 and 37 for different colors
            print(f"\033[{color_code}m{digit}\033[0m", end="")

        print()
        print("Attempts")

        break
    elif RandomNumber > UI:
        print("\033[91mtoo high\033[0m")
    elif RandomNumber < UI:
        print("\033[91mtoo low\033[0m")

