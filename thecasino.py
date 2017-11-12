import sys

def guessingGame(balance):
    # This is a guess the number game.
     import random

     guessesTaken = 0

     number = random.randint(1, 20)
     print("I am thinking of a number between 1 and 20.")

     while guessesTaken < 6:
         print('Take a guess.')
         guess = input()
         guess = int(guess)

         guessesTaken = guessesTaken + 1

         if guess < number:
             print('Your guess is too low.')

         if guess > number:
             print('Your guess is too high.')

         if guess == number:
             break

     if guess == number:
         guessesTaken = str(guessesTaken)
         print('Good job, You guessed my number in ' + guessesTaken + ' guesses!')

     if guess != number:
         number = str(number)
         print('Nope. The number I was thinking of was ' + number)

def craps(balance):
    print("Coming Soon")


def help():
    print "\nGAMES: \n 1 - Guessing Game \n 2 - Craps \n 3 - In Between \n 4 - Help \n 5 - Quit"
    print "HOW TO PLAY: \n \nGUESSING GAME: \nThe goal of the Guessing Game is pretty simple. You are to guess a number between 1 and 20. You will continue to \nguess to you reach the number. Your pay out is determined by how many tries you take to guess the number.\n"
    print "CRAPS: \n Coming Soon!\n"
    print "IN BETWEEN: \n Coming Soon!\n"

def end():
    sys.exit()

def main():
    balance = 100
    print "Welcome to the Python casino! What would you like to do?"
    print "\n 1 - Guessing Game \n 2 - Craps \n 3 - In Between \n 4 - Help \n 5 - Quit"
    choice = 0
    while choice != 5:
        choice = input("Enter 1-5 to choose what you want to do: ")
        if choice == 1:
            balance = guessingGame(balance)
        elif choice == 2:
            balance = craps(balance)
        elif choice == 3:
            balance = inBetween(balance)
        elif choice == 4:
            help()
        elif choice == 5:
            end()
main()
