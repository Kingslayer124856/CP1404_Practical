

import random
NUMBER_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    Number_of_picks = input("How many qick picks? ")
    while Number_of_picks <= '0' :
        print("What?")
        Number_of_picks = input("How many quick picks? ")

    for i in range(Number_of_picks):
        quick_pick = []
        for j in range(NUMBER_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in guick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{2}".format(number) for number in quick_pick))
main()