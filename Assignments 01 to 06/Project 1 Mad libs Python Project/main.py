

def main():
    name = input("Enter your name: ")
    print(f"Good! So {name} here is my Mad lib game based on little story.")
    print()

    adjective = input("Enter an adjective (e.g: spicy, sweet, delicious): ")
    plu_noun = input("Enter a plural noun (e.g: sandwiches, cookies, chocolates): ")
    adjective2 = input("Enter second adjective (e.g: spicy, seweet, delicious): ")
    noun = input("Enter a noun (e.g: sauce, juice, cheese): ")
    adjective3 = input("Enter third adjective (e.g: yummy, spicy, delicious): ")
    print()
    print("Here is the story...")
    print()
    print(f"I like to eat {adjective} {plu_noun}.")
    print(f"They taste very {adjective2} with some {noun}.")
    print(f"It makes me feel {adjective3}.")

    print()

if __name__ == "__main__":
    main()
