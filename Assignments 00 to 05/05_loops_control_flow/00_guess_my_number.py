#Guess My Number
#I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
#Enter a new number: 25 Your guess is too low
#Enter a new number: 40 Your guess is too low
#Enter a new number: 45 Your guess is too low
#Enter a new number: 48 Congrats! The number was: 48


import random

def main():
    print("I am thinking of a number between 1 and 99...")
    while True:

        random_number = random.randint(1,99)
     
        user_input = int(input("Enter a new number: "))
        
        if random_number == user_input:
            print(f"Congrats! The number was: {random_number}")
            break
        elif user_input > random_number:
            print(f"{user_input} Your guess is too high")

        else:
            print(f"{user_input} Your guess is too high")
        print()

if __name__ == '__main__':
    main()