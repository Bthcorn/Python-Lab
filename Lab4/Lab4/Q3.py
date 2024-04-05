import random
user = int(input("scissor(0), rock(1), paper(2): "))
game = ["scissor", "rock", "paper"]
computer = random.choice(game)


if computer == "scissor":
    if user == 0:
        print("The computer is scissor. You are scissor. It is a draw.")
    elif user == 1:
        print("The computer is scissor. You are rock. You won.")
    elif user == 2:
        print("The computer is scissor. You are paper. You lost.")
elif computer == "rock":
    if user == 0:
        print("The computer is rock. You are scissor. You lost.")
    elif user == 1:
        print("The computer is rock. You are rock. It is a draw.")
    elif user == 2:
        print("The computer is rock. You are paper. You won.")
elif computer == "paper":
    if user == 0:
        print("The computer is paper. You are scissor. You won.")
    elif user == 1:
        print("The computer is paper. You are rock. You lost.")
    elif user == 2:
        print("The computer is paper. You are paper. It is a draw.")