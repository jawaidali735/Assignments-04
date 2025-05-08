# ans of question 2 
# creating a phone book with name and numbers

def get_phonebook():

    phonebook= {}

    while True:
        name = input("Enter a name: ")

        if name == "":
            break

        number = input("Enter a number: ")
        phonebook[name] = number
    
    return phonebook


def print_phonebook(phonebook):

    for name in phonebook:

        print(str(name) + " ->" + str(phonebook[name]) )


def lookup_numbers(phonebook):

    while True:
        name = input("enter a name: ")

        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name]);


def main():
    phonebook = get_phonebook()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

    print(phonebook)

if __name__ == "__main__":
    main()