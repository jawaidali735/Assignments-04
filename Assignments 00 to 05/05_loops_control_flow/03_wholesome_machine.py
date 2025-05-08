#Ans of question 03 in loops control flow


AFFIRMATION : str = "I am capable of doing anything I put my mind to."


def main():
    print("Please enter the following affirmation:", AFFIRMATION)
    user_input = input("Enter here: ")

    while user_input != AFFIRMATION:
        print("That was not the affirmation.")

        print("Please enter the following affirmation:", AFFIRMATION)
        user_input = input("Enter here: ")
    
    print("That's right!")
if __name__ == '__main__':
    main()