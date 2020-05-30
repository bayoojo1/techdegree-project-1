from random import randint
import sys

highest_score = ''
attempts = []

def start_game():
    while True:
        random_number = randint(1, 9)
        guesses = 0
        while True:
            try:
                answer = int(input("What is the winning number? (Guess between number 1 - 9) "))
                guesses += 1
                
                if answer > 9 or answer < 1:
                    raise ValueError("That's not a valid number! Try again please.")
            except ValueError:
                print("You can only enter digit between 1 - 9 please!")
            else: 
                if answer == random_number:
                    print("You are correct! The winning number is {}.\nYou got it after {} attempt(s)".format(answer, guesses))
                    attempts.append(guesses)
                    highest_score = min(attempts)
                    break
                elif answer > random_number:
                    print("It's lower!")
                elif answer < random_number:
                    print("It's higher!")
                       
        if input("Do you want to play again? [y]es or [n]o ").lower() == 'y':
            #print(attempts)
            print("The HIGHEST SCORE is {} attempts".format(highest_score))
            continue
        else:
            break
            
                
    print("Thanks for your participation. See you again some other time.")
    sys.exit()
        

while True:
    print("""
           -------------------------------------
           Welcome to the number guessing game!
           -------------------------------------
                      Instruction:
           1. I'm holding a number between 1 and 9
           2. You need to guess the number by typing your choice at the prompt
           3. Continue to make a guess until you get the correct answer
           
    """)
    if input("Do you want to give it a try? [y]es or [n]o ") == 'y':
        start_game()
    else:
        break