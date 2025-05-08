import random
def guess_by_comp(x):
    print("--> Guess a number between 1, 20 <--")
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} is too high (H), too low (L), or correct (C): ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yeah! The computer guessed your number, {guess} correctly.")

guess_by_comp(20)