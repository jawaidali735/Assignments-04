# add two numbers

# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

# The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.

# so now we have to take inputs froms users and sum up 


first_number = input("enter the first number:")
convert_to_int = int(first_number)

secand_number = input("enter the second number:")
convert_sec_to_int = int(secand_number)

def calculate_sum(first, second):
   sum = first + second
   
   return sum



if __name__ == "__main__":  # this is a safe guard
    print("The total sum is:",calculate_sum(convert_to_int, convert_sec_to_int))   
    