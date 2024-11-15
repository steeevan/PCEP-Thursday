# use the pythons random module to generate the computers chouce
import random # The random module allows the program to randomly pick.

# The list contains valid chocies for the game
options = ["rock", "paper", "scissors"]

# variables keep track of wins for the user and computer
user_score = 0
computer_score = 0

# Create a function to get users choice
'''
Purpose: Prompt the user to select Rock Paer or Scissors
Use the input() to ask the user for their choice
you could use the lower method to minimize all letters or capitlize() method with strings
The input should be in strings
If the user enters something that is not part of optinos we should re ask them again to enter 
something properly

Hint - while loop to validate the data entered
'''
def get_user_choice():
    while True:
        choice = input("Enter Rock, Paper, Scissors: ").lower()
        if choice in options:
            return choice
        else:
            print("Invalid Choice. Please try again")


'''
Create a function that returns the computers choice
YOu will randomly select an item from the options list and return that
'''
def get_computer_choice():
    return random.choice(options)
'''
Create a functino to determine the Winner
Use conditional statements to compare the users and computer choices to decide the winner

'''
def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    elif (user =="rock" and computer == "scissors") or \
        (user == "scissors" and computer == "paper") or \
        (user == "paper" and computer == "rock"):
        return "User Wins"

    else:
        return "Computer Wins"



'''
Create a function to show the users and computers choices and announce the winner
Using the f string format

'''
def display_results(user,computer,winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if winner == "Tie":
        print("Its a tie!")
    elif winner == "User Wins":
        print("User wins this round")
    else:
        print("Computer wins this round")


# Lets make our game logic
def play_game():
    global user_score, computer_score
    play_again = True
    while play_again:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice,computer_choice)

        if winner == "User Wins":
            user_score += 1
        elif winner == "Computer Wins":
            computer_score += 1
        display_results(user_choice,computer_choice,winner)

        print(f"Score - You: {user_score} -------- Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for Playing")
            play_again = False
            
play_game()