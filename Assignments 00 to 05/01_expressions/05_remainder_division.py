#Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
#The result of this division is 1 with a remainder of 2.

def main():
    divid_to_be = int(input("Please enter an integer that you want to be divided: "))
    divid_by = int(input("Please enter an integer that you want to divid by: "))

    division = (divid_to_be // divid_by)
    remainder = divid_to_be % divid_by

    print(f"The result of this division is {division} with a remainder of {remainder}")


if __name__ == "__main__":
    main()