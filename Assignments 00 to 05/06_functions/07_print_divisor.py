#Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1 to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!


def divisor(num):
    print("Here are the divisors of", num)
    for i in range(10):
        current_num = i + 1

        if num % current_num  == 0:
            print(current_num)


def main():
    num = int(input("Enter a number "))
    divisor(num)

if __name__ == '__main__':
    main()