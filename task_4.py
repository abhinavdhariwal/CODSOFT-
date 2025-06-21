# Rock Paper Scissors Game using Python
# Developed by Abhinav (Intern @CodSoft)

import random

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors Game!")
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose rock, paper or scissors (or type 'exit' to stop): ").lower()
        if user_choice == 'exit':
            break
        if user_choice not in choices:
            print("Invalid choice! Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Scores - You: {user_score}, Computer: {computer_score}")
        print("-" * 30)

    print("Thanks for playing!")

# Run the game
rock_paper_scissors()