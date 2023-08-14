'''Comp guesses User number

This program will guess a number of your choice within a range utilizing binary iteration.

by Dallin Hull '''
import math
import statistics

# Get user's name

user_name = input('Hi, what is your name? ')

def greeting_and_instructions(name):
    print()
    print(f"{name} did you say? Well, I'm excited to play with you!")
    print()
    print("So here's how you play:")
    print("You will choose a number in your head, and I will try to guess it.")
    print("Before I start to guess, you'll select a lower limit and an upper limit, like 1 and 100 or 533 and 1237. Whatever you want!")
    print("Once you think of a number within your limits, then I'll start guessing.")
    print("After each guess, you'll type whether your number was 'higher', 'lower', or 'correct'.")
    print("Guaranteed that I'll figure out your number in 10 guesses or less!")
    print()

'''    print("Here's how we get started: ")
    print("First, we'll define a lower limit and an upper limit to a range of numbers.")
    print("Next, you'll choose a unique number WITHIN the limit we just created")
    print(f"Then, I try to guess the number that you chose. Sounds like fun right, {name}!?")
    print()
    print("Oh and to make things interesting, after every guess you'll tell me whether your chosen number \n is higher then, lower then, or the same as your chosen number.")
    print()'''
    
def lower_limit():
    while True:
        print()
        lower = input("Okay, what number do you want to be your lower limit? ")
        try:
            lower = int(lower)
        except:
            print("Please enter your input numerically and as an integer (don't worry about those pesky commas).")
            continue
    
        if lower <=0:
            print("Umm... this is awkward, but I only know positive numbers. Please \n enter a number that is higher than 0")
            continue
        
        elif lower >= 2000:
            print("Sorry, but I can't count that high. Can you try something less than 2000?")
            continue
            
        else:
            #acceptable = True
            return lower
        
def upper_limit(num):
    while True:
        print()
        upper = input("And what number do you want to be your upper limit? ")
        print()
        try:
            upper = int(upper)
        except:
            print("Please enter your input numerically and as an integer (don't worry about those pesky commas).")
            continue
    
        if upper <= num:
            print('I mean, this number kinda has to higher than the last one you chose...')
            continue
            
        if upper > 2000:
            print("Umm... this is awkward, but I only know numbers up to 2000")
            continue
            
        else:
            #acceptable = True
            return upper  
        
'''def user_choice(lower_num, upper_num):
    while True:
        print()
        user_num = input(f"So your lower limit is {lower_num} and your upper limit is {upper_num}.\n Now choose the number you want me to guess! ")
        try:
            user_num = int(user_num)
        except:
            print("Please enter your input numerically and as an integer (don't worry about those pesky commas).")
            continue
    
        if user_num < lower_num:
            print('I mean, this number kinda has to higher than the lower limit you chose...')
            continue
            
        if user_num > upper_num:
            print("Umm... this is awkward, but this number has to be lower than the upper limit you chose...")
            continue
            
        else:
            #acceptable = True
            return user_num 
'''

def comp_guess(lower_number, upper_number):
    print("Awesome let's start!")
    print()
    feedback = ""
    congrats_phrase = "Dude, finally."
    while feedback != "correct":
        
        if lower_number == upper_number - 1:
            guess = upper_number
            feedback = input(f"Is your number higher or lower than {guess}? or is it correct? ").lower()
            print()
            
            if feedback == "lower":
                upper_number = guess - 1
                continue
            if feedback == "higher":
                lower_number = guess + 1
                continue
            if feedback == "correct":
#                print("Dude, finally.")
                break
        elif lower_number == upper_number:
            guess = upper_number
            feedback = input(f"Is your number {guess}? Type 'correct' (cuz I know I'm right ;) ) ").lower()
        else:
#            print(lower_number, ", ", upper_number)
            guess = math.ceil(statistics.median(range(lower_number, upper_number)))
            feedback = input(f"Is your number higher or lower than {guess}? or is it correct? ").lower()
            print()
                
            if feedback == "lower":
                upper_number = guess - 1
                continue
            if feedback == "higher":
                lower_number = guess + 1
                continue
            if feedback == "correct":
#                print("Dude, finally.")
                break
    return congrats_phrase
                
    
            
greeting_and_instructions(user_name)

play_again = "yes"

while play_again == "yes":
    
    

    lower_number = lower_limit()

    upper_number = upper_limit(lower_number)

#user_choice = user_choice(lower_limit, upper_limit)

    computer_guess = comp_guess(lower_number, upper_number)

    print(computer_guess)
    
    print()
    play_again = input("Would you like to play again? yes/no: ").lower()
    
print(f"Well that was fun, {user_name}. Come back and play again soon.")


# Have them select UPPER limit and LOWER limit to create a range
'''
THOSE NUMBERS MUST HAVE THESE CHARACTERISTICS

> Integer
>>> If float, string, contains comma, etc then inform user and ask them to reselect an integer

> Greater than or equal to 0
>>> If neg num, inform user and ask them to reselect

> More?
'''

# Have them select a num within the range
'''
THE NUMBER MUST HAVE THESE CHARACTERISTICS

> Integer
>>> If float, string, contains comma, etc then inform user and ask them to reselect an integer

> Greater than or equal to 0
>>> If neg num, inform user and ask them to reselect

> Double check with Roger that it's in the range
'''
# End of program when number guessed correctly
# Ask if user wants to play again


# Computer guess logic
'''
> identify median of range
> Ask user if number is correct, higher, or lower
>>> IF Higher
------ Count up 1 from guess
------ Redefine lower limit of range
------ Loop computer guessing logic
>>> IF LOWER
------ Count down 1 from guess
------ Redefine upper limit of range
------ Loop computer guessing logic
>>> IF CORRECT
------ Run End of Program
'''