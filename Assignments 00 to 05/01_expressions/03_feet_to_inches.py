#Converts feet to inches. Feet is an American unit of measurement. 
# There are 12 inches per foot. Foot is the singular, and feet is the plural.

def main():

    feet = int(input("Enter feet to convert into inches: "))

    convert_into_inches = feet * 12
    converted_value = "\033[1;3m" + str(convert_into_inches) + "\033[0m"

    print(str(feet) + " feet is equal to " + str(converted_value) + " inches")




if __name__ == '__main__':
    main()