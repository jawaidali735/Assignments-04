import random

def play():
    print("What's your choice?")
    rounds = 0
    while rounds < 3:  # Game will stop after 3 rounds
        user = input("'r' for rock, 'p' for paper, 's' for scissor\n")
        if user == "":
            print("Game over!")
            break
        
        computer = random.choice(['r', 'p', 's'])
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a Tie!")
        elif is_win(user, computer):
            print("You won!")
        else:
            print("You lost!")
        
        rounds += 1  # Increment round after each game

    if rounds == 3:
        print("Game Over. Thanks for playing!")

def is_win(player, opponent):
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

if __name__ == "__main__":
    play()
