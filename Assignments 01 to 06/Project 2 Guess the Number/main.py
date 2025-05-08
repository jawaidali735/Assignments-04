import random 

def guess_number():
    print("Welcome to the number guessing game.")
    print("I'm thinking a number between 1 to 100")
    number = random.randint(1, 100)
    guesses_left = 7
    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        try: 
            guess = int(input("Take a guess: "))
        except ValueError: 
            print("Invalid input: Please enter a number")
            continue


        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else: 
            print("Congrats! You guessed correct number.")

        guesses_left -= 1
        print()
    print(f"You ran out of guess. The number was {number}")

if __name__ == "__main__":
    guess_number()