#Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.
#Here's a sample run (user input is in blue):
#Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']


def main():
    my_list = []
    element = input("Enter a value: ")

    while element != "":
        my_list.append(element)
        element = input("Enter a value: ")

        if (element == ""):
            print(my_list)



if __name__ == '__main__':
    main() 