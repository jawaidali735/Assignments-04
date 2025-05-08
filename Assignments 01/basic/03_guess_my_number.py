#solution of question 03 in basic


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