#High-Low Game

import random

def guess_game():
    print("\n" + "="*40)
    print("🎮  Welcome to the High-Low Game!  🎲")
    print("="*40 + "\n")


    your_score = 0
    for i in range(5):
        
        print("Round", i + 1)

        computer_number = random.randint(1,100)
        your_number = random.randint(1,100)
        print("Your Number:",your_number)
        user_input = input("What do you think that your number is higher or lower: ")
        user_input = user_input.strip().lower()
        
        if   user_input == "higher" and your_number > computer_number:
            print("You were right! The computer's number was", computer_number)
            your_score += 1
           
        elif user_input == "lower" and your_number < computer_number:
            print("You were right! The computer's number was", computer_number)
            your_score += 1
            
        else:
            print("Aww, that's incorrect. The computer's number was", computer_number)
            
        print("Your score is now", your_score)
        print()
    
    print("\n" + "="*44)
    print("🎉  Thanks for playing! Come back soon!  🙌")
    print("="*44)


def main():
    guess_game()


if __name__ == "__main__":
    main()