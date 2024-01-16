import random

def randomNumber():
    targetNumber = random.randint(1, 100)
    return targetNumber

def getAttempts(attmepts):
    print(f"You have {attmepts} left to guess the right number.")

def compare_guess(guess, target):
    if guess == target:
        print("You win!")
        return True
    if guess < target:
        print("Too low.")
    if guess > target:
        print("Too high.")
    return False

def run_game():
    print("Welcome to the Number Guessing Game.")
    print("I am thinking of a number 1 through 100.")
    target = randomNumber()
    choose_mode = input("Choose a difficulty. Type 'easy' or 'hard': " )
    if choose_mode == 'easy':
        starting_attempts = 10
    else:
        starting_attempts = 5
    
    while starting_attempts > 0:
        getAttempts(starting_attempts)
        guess = int(input("Make a guess: "))
        check_guess = compare_guess(guess, target)
        if check_guess == True:
            play_again = input("Play again? Type 'yes' or 'no': ")
            if play_again == 'yes':
                run_game()
            else:
                print('Thanks for playing.')
                starting_attempts = -1
                break
        else:
            starting_attempts -= 1
        


run_game()