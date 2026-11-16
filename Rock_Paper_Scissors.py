import random

game = ['rock', 'paper', 'scissors']

while True:
    user_input = input("rock, paper, or scissors?: ").lower()

    bot_play = random.choice(game)
    print("-------------------")
    print(f"You played {user_input}")
    print(f"Bot played {bot_play}")
    print("-------------------")

    if user_input == bot_play:
        print("Tie! ")
    elif user_input == "rock":
        if bot_play == "paper":
            print("You Lose!")
        elif bot_play == "scissors":
            print("You Win!")
    elif user_input == "paper":
        if bot_play =="rock":
            print("You Win!")
        elif bot_play =="scissors":
            print("You Lose!")
    elif user_input == "scissors":
        if bot_play =="rock":
            print("You Lose!")
        elif bot_play =="paper":
            print("You Win!")
    else: print("What you entered was invalid!")
    print("-------------------")
    again = input("Would you like to play again? (yes/no): ").lower()
    if again == "no":
        break

print("Have a good day!")