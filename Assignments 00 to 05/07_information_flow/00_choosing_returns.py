#There are times where we want to return different things from a function based on some condition. To practice this idea, imagine that we want to check if someone is an adult. We might check their age and return different things depending on how old they are!
#We've provided you with the ADULT_AGE variable which has the age a person is legally classified as an adult (in the United States). Fill out the is_adult(age) function, which returns True if the function takes an age that is greater than or equal to ADULT_AGE. If the function takes an age less than ADULT_AGE, return False instead.



adult_age = 18

def is_adult(age):

    if age >= adult_age:
        return True
    return False

    

def main():

    age = int(input("How old are you: "))

    if is_adult(age):
       print("You are an adult.")
    else:
        print("You are not an adult.")


if __name__ == "__main__":
    main()