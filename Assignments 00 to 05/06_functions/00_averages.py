#Write a function that takes two numbers and finds the average between the two.


def average_number(num1, num2):
    
    average = num1 + num2
    return average / 2

def main():

    first_ave = average_number(2,3)
    second_ave = average_number(3,4)

    total = average_number(first_ave,second_ave)

    print(first_ave)
    print(second_ave)
    print(total)

if __name__ == '__main__':
    main()