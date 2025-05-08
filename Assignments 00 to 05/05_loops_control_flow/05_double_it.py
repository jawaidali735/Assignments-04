#solution of question 05 in loops control flow

def main():
    user_input = int(input("enters a number: "))

    while user_input < 100:

        user_input = user_input *2
        print(user_input)


if __name__ == '__main__':
    main()