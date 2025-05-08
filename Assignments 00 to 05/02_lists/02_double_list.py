#Write a program that doubles each element in a list of numbers. For example, if you start with this list:
#numbers = [1, 2, 3, 4]
#You should end with this list:
#numbers = [2, 4, 6, 8]


def list_doubled():
    numbers = [1,2,3,4]

    print([x*2 for x in numbers])

if __name__ == "__main__":
    list_doubled()

#it can aslo be done like this


def main():
    numbers:list[int] = [1,2,3,4]

    for i in range(len(numbers)):

        elements = numbers[i]
        numbers[i] = elements * 2
    print(numbers)


if __name__ == '__main__':
    main()         


