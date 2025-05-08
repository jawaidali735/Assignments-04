# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!




def main():
    
    user_Input = input("What is you favorite animal name?")
    animal_name = "\033[1;3m" + user_Input + "\033[0m"
    print(f"My favorite animal is also {animal_name}!")

if __name__ == "__main__":
    main() 







#we can also do this with loop:
def main():
    

    while True:
        user_Input = input("What is you favorite animal name?")
        

        if user_Input == "exit" :
            break
        else:
            animal_name = "\033[1;3m" + user_Input + "\033[0m"
            print(f"My favorite animal is also {animal_name}!")

if __name__ == "__main__":
    main() 