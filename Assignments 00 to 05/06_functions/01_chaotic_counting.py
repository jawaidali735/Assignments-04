#solution of question 01 in functions


import random
stopping_number = 0.3

def chaotic_counting():

    for i in range(10):
        current_value = i + 1
        if done():
            return
        print(current_value)


def done():
     random_numbers = random.random()
     if random_numbers < stopping_number:
         return True
     return False

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
