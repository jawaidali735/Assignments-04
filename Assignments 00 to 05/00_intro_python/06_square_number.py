#Ans of Q6
#Ask the user for a number and print its square (the product of the number times itself).

def main():

    user_input = float(input("Want to know square? Type a number: "))
    square = user_input **2   
    print(f"{user_input} squared is {square}")

if __name__ == "__main__":
    main()