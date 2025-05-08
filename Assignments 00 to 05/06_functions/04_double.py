#Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.

def double(num):

    doubled = num * 2
    return doubled


def main():

    user_Input = int(input("Enter a number: "))
    doubled_number = double(user_Input)

    print("Double that is", doubled_number)

if __name__ == '__main__':
    main()
