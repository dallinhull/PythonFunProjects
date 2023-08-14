""" Rock, Paper, Scissors, Lizard, Spock
By Dallin Hull"""

import random

possible_actions = ["rock", "paper", "scissors", "lizard", "spock"]

class Rock:
    scissors = "Rock crushes Scissors. You WIN this round."
    lizard = "Rock crushes Lizard. You WIN this round."
    paper = "Paper covers Rock. You LOSE this round."
    spock = "Spock vaporizes Rock. You LOSE this round."
    rock = "We TIE this round. No points awarded."
    
class Paper:
    rock = "Paper covers Rock. You WIN this round."
    spock = "Paper disproves Spock. You WIN this round."
    scissors = "Scissors cut Paper. You LOSE this round."
    lizard = "Lizard eats Paper. You LOSE this round."
    paper = "We TIE this round. No points awarded."
    
class Scissors:
    paper = "Scissors cut Paper. You WIN this round."
    lizard = "Scissors decapitates Lizard. You WIN this round"
    rock = "Rock crushes Scissors. You LOSE this round."
    spock = "Spock smashes scissors. You LOSE this round."
    scissors = "We TIE this round. No points awarded."
    
class Lizard:
    paper = "Lizard eats Paper. You WIN this round."
    spock = "Lizard poisons Spock. You WIN this round."
    rock = "Rock crushes Lizard. You LOSE this round."
    scissors = "Scissors decapitates Lizard. You LOSE this round."
    lizard = "We TIE this round. No points awarded."
    
class Spock:
    rock = "Spock vaporizes Rock. You WIN this round."
    scissors = "Spock smashes Scissors. You WIN this round."
    paper = "Paper disproves Spock. You LOSE this round."
    lizard = "Lizard poisons Spock. You LOSE this round."
    spock = "We TIE this round. No points awarded."


check_result = {"rock": Rock, "paper": Paper, "scissors": Scissors, "lizard": Lizard, "spock": Spock}


help = "\nRock, Paper, Scissors, Lizard, Spock is just like the original Rock, Paper, Scissors but with a fun twist.\n\
            You and I will choose a weapon and reveal it at the same time. \n\
            If your weapon beats mine, then you win! And vice versa.\n\
            \n\
            Weapons defeat each other in this manner:\n\
            \n\
            Scissors cuts Paper\n\
            Paper covers Rock\n\
            Rock crushes Lizard\n\
            Lizard poisons Spock\n\
            Spock smashes Scissors\n\
            Scissors decapitates Lizard\n\
            Lizard eats Paper\n\
            Paper disproves Spock\n\
            Spock vaporizes Rock\n\
            \n\
            and as it always has\n\
            \n\
            Rock crushes Scissors\n\
            \n\
            The winner of each round will gain a point until someone gains enough points to win the game. Clear as mud?"


def greeting(user_name):
    print(f"\n{user_name} is such a fabulous name!")


def guage_experience():
    while True:
        print()
        experienced_user = input("Have your played this game before? yes/no ")
        if experienced_user.lower() == "yes":
            print()
            print("We'll skip the rules for now then, but you can always review them by typing 'help'.")
            break
        elif experienced_user.lower() == "no":
            print(help)
            break
        else:
            print()
            print("Please type 'yes' or 'no'.")
            continue


def win_condition_selection():
    while True:
        print()
        winning_point = input("So let's play! How many points does the winner need to get? ")
        try:
            winning_point = int(winning_point)
        except:
            if winning_point == "help":
                print(help)
                continue
            else:
                print()
                print("Please enter a number between 1-10 in numerical form.")
                continue
        
        if int(winning_point) > 10:
            print()
            print("Please enter a number between 1-10 in numerical form.")
            continue
        elif int(winning_point) < 1:
            print()
            print("Please enter a number between 1-10 in numerical form.")
            continue
        else:
            winning_point = int(winning_point)
            print()
            print(f"Great! It'll be a first-to-{winning_point}. I'll keep track as we play.")
            print()
            break
    return winning_point


def play_game(winning_score, possible_actions, check_result):
    player_score = 0
    computer_score = 0
    print("Player : ", player_score, " | ", computer_score, " : Computer")
    while player_score != winning_score and computer_score != winning_score:
        computer_choice = random.choice(possible_actions)
        print()
        player_choice = input("Select your weapon: ")
        if player_choice == "help":
            print(help)
            continue
        
        elif player_choice == "gun":
            print()
            print("Hahaha just as funny as the other 3rd graders! Let's get back to the game, shall we?")
            continue
        
        elif player_choice not in possible_actions:
            print()
            print("Please choose between rock, paper, scissors, lizard, spock")
            print()
            print("Player : ", player_score, " | ", computer_score, " : Computer")
            continue
            
        player_choice = player_choice.lower()
        result = getattr(check_result[player_choice], computer_choice)
        print(f"\nYou chose {player_choice}, computer chose {computer_choice}. {result}\n")
        if "WIN" in result:
            player_score += 1
        elif "LOSE" in result:
            computer_score += 1
        print("Player : ", player_score, " | ", computer_score, " : Computer")
        
    if player_score == winning_score:
        print()
        print("Congrats, you win!")
    else:
        print()
        print("Better luck next time!")



user_name = input("Let's play Rock, Paper, Scissors, Lizard, Spock together! But first, what's your name? ")
       
greeting(user_name)

guage_experience()

play_again = "yes"

while play_again == "yes":
    
    winning_score = win_condition_selection()
    
    play_game(winning_score, possible_actions, check_result)
    
    print()
    play_again = input("Would you like to play again? yes/no ").lower()

print(f"Well that was fun, {user_name}. Come back and play again soon.")