#Simulate rolling two dice, and prints results of each roll as well as the total.


import random

def main():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    total = dice1 + dice2

    print(f"Die 1: {dice1}")
    print(f"Die 2: {dice2}")

    print(f"The total of dice is: {total}")


if __name__ == "__main__":
    main()
