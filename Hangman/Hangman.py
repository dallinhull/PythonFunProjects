''' Hangman
by Dallin Hull
'''
import random

import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word


def wrong_guess_limit_selection():
    print()
    difficulty_options = [10, 8, 6, 5, 3]
    difficulty = 0
    while True:
        difficulty = input("At what difficulty would you like to play? This will determine how many wrong guesses you get:\n\
                            For Beginner,     type '10' to allow for 10 wrong guesses.\n\
                            For Easy,         type '8' to allow for 8 wrong guesses.\n\
                            For Intermediate, type '6' to allow for 6 wrong guesses.\n\
                            For Hard,         type '5' to allow for 5 wrong guesses.\n\
                            For Insane,       type '3' to allow for 3 wrong guesses.\n\
                            \n\
                            Type your answer here: ")
        
        try:
            difficulty = int(difficulty)
        except:
            print()
            print("Please type '10' , '8' , '6' , '5' , or '3' numerically to continue.")
            continue
        
        if int(difficulty) not in difficulty_options:
            print()
            print("Please type '10' , '8' , '6' , '5' , or '3' to continue.")
            continue
        
        else:
            print()
            print("Good choice!")
            print()
            return int(difficulty)


def game(word, wrong_guess_ceiling):
    word_array = []
    letters_available = [*string.ascii_lowercase]
    letters_already_guessed = []
    wrong_guesses = 0
    wrong_guess_limit = wrong_guess_ceiling
    for letter in word:
        word_array.append("_")
    

    while "_" in word_array and wrong_guesses < wrong_guess_limit:
        print()
        print(*word_array)
        print()
        print(f"Letters left: {letters_available}")
        print(f"Letters already guessed: {letters_already_guessed}")
        print("Guesses left: ", wrong_guess_limit - wrong_guesses)
        print()
        current_guess = input("Type a letter and press Enter: ").lower()
        
        if len(current_guess) != 1:                      #make sure only one character
            print()
            print("You may guess one letter at a time. ")
            continue
        
        elif current_guess not in string.ascii_lowercase: #make sure it is a letter
            print()
            print("Please guess a letter from a-z. ")
            continue
        
        elif current_guess in letters_already_guessed:  #make sure first time guessing letter
            print()
            print(f"{current_guess} has already been guessed. You may choose a different number.")
            continue
            
        elif current_guess not in word: #Check if secret word does NOT contain current_guess. add wrong guess and append to letters_already_guessed
            print()
            print()
            print(f"The secret word does not contain {current_guess}")
            wrong_guesses += 1
            letters_available.remove(current_guess)
            letters_already_guessed.append(current_guess)
            letters_already_guessed.sort()
            continue
        
        elif current_guess in word:    #Check if valid guess. Word_array add correct letters in correct index(es). append current_guess to letters_already_guessed
            print()
            print()
            print("You got one!")
            letters_available.remove(current_guess)
            letters_already_guessed.append(current_guess)
            letters_already_guessed.sort()
            for index,character in enumerate(word):
                if character == current_guess:
                    word_array[index] = current_guess
        
        else:
            print()
            print("Unknown problem")
            continue
            
    if wrong_guesses == wrong_guess_limit:
        print()
        print("Looks like you many too many wrong guesses. Better luck next time!")
        print()
        print(f"The word was '{valid_word}'")
        
    else:
        print()
        print(f"Great job! The word was '{valid_word}'. You crushed that silly word.")
        
        

print("Let's play Hangman! ")
print()

play_again = "yes"

while play_again == "yes":
    
    valid_word = get_valid_word(words)
    word = valid_word.upper()
    word = list(valid_word)
    
    wrong_guess_limit = wrong_guess_limit_selection()
    
    game(word, wrong_guess_limit)
    
    print()
    play_again = input("Would you like to play again? yes/no ").lower()

print(f"Well that was fun. Come back and play again soon.")