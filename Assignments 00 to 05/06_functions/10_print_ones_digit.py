#Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!



def print_ones_digit(num):
    print(num % 10) # to use 10 to take out last digit of number no matter its big number or small and we use 2 
                    #to check that number is completly dividble or not, and to check odd and even.


def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == "__main__":
    main()