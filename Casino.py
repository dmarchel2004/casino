#The Casino
#Dylan and Avi

from random import *
import os
import time

def guessingGame(balance):
    os.system("clear")
    bet = betty(balance)
    os.system("clear")
    guessesTaken = 1
    number = randint(1,40)
    print("I am thinking of a number between 1 and 40.")
    while guessesTaken < 6:
        guess = raw_input('Take a guess: ')
        if guess.isdigit():
            guess = int(guess)
            if guess < number:
                print('Your guess is too low.')
            if guess > number:
                print('Your guess is too high.')
            if guess == number:
                guessesTaken = str(guessesTaken)
                print('Good job, you guessed my number in ' + guessesTaken + ' guesses!')
                print "You won five times your bet,", bet * 5, "dollars."
                balance = balance + (bet * 5)
                print "Your current balance is", balance
                return balance
            guessesTaken = guessesTaken + 1
        if guessesTaken == 6:
            print "The number was", number
            print "You lost", bet, "dollars."
            balance = balance - bet
            print "Your current balance is $",balance
            return balance

def craps(balance):
    os.system("clear")
    bet = betty(balance)
    os.system("clear")
    start = raw_input('Press "enter" to roll the dice: ')
    die1 = randint(1,6)
    die2 = randint(1,6)
    dsum = die1 + die2
    dsumFirst = dsum
    running = True
    tries = 1
    while running:
        print "First is", dsumFirst
        print "You rolled", dsum
        if dsum in [2,3,12]:
            balance = balance - bet
            print "You lost", bet, "dollars. \n Your current balance is $",balance
            return balance
        elif dsum in [7,11]:
            balance = balance + (bet * 3)
            print "You won three times your bet,", bet * 3, "dollars. \n Your current balance is $",balance
            return balance
        else:
            if tries > 1 and dsum == dsumFirst:
                balance = balance + (bet * 3)
                print "You won three times your bet,", bet * 3, "dollars. \n Your current balance is $",balance
                return balance
            else:
                print "You didn't win or lose."
                start = raw_input('Press "enter" to roll the dice: ')
                die1 = randint(1,6)
                die2 = randint(1,6)
                dsum = die1 + die2
                tries += 1

def inBetween(balance):
    os.system("clear")
    bet = betty(balance)
    os.system("clear")
    card1 = randint(1,13)
    card2 = randint(1,13)
    cards = [card1, card2]
    cards.sort()
    cardGuess = 0
    while cardGuess == 0:
        cardGuess = raw_input("Guess a card to see if it is between one of the cards chosen. (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King): ")
        if cardGuess == "Ace":
            cardGuess = 1
            cardPass = 1
        elif cardGuess == "Jack":
            cardGuess = 11
            cardPass = 1
        elif cardGuess == "Queen":
            cardGuess = 12
            cardPass = 1
        elif cardGuess == "King":
            cardGuess = 13
            cardPass = 1
        else:
            if cardGuess.isdigit():
                cardGuess = int(cardGuess)
                cardPass = 1
                print cardGuess
            else:
                print "That is not a valid guess."

    if cardGuess > min(cards) and cardGuess<max(cards):
        if card1 == 1:
            card1 = "Ace"
        elif card1 == 11:
            card1 = "Jack"
        elif card1 == 12:
            card1 = "Queen"
        elif card1 == 13:
            card1 = "King"
        if card2 == 1:
            card2 = "Ace"
        elif card2 == 11:
            card2 = "Jack"
        elif card2 == 12:
            card2 = "Queen"
        elif card2 == 13:
            card2 = "King"
        print "The cards were", card1, "and", card2
        balance = balance + (bet * 3)
        print "You won three times your bet,", bet * 3, "dollars. \n Your current balance is $",balance
        return balance
    else:
        if card1 == 1:
            card1 = "Ace"
        elif card1 == 11:
            card1 = "Jack"
        elif card1 == 12:
            card1 = "Queen"
        elif card1 == 13:
            card1 = "King"
        if card2 == 1:
            card2 = "Ace"
        elif card2 == 11:
            card2 = "Jack"
        elif card2 == 12:
            card2 = "Queen"
        elif card2 == 13:
            card2 = "King"
        print "The cards were", card1, "and", card2
        balance = balance - bet
        print "You lost", bet, "dollars. \n Your current balance is $",balance
        time.sleep(3)
        return balance

def directions():
    os.system("clear")
    print "\n HOW TO PLAY: \n"
    print "GUESSING GAME: \n You are to guess a number between 1 and 20. You will continue for five guess or if you get the number. If you haven't guessed the number after five guesses you lose.\n"
    print "CRAPS: \n You will roll two die. If the sum of both die is 2, 3, or 12, you lose. If the sum is 7 or 11 you win. After the first roll, if at any time the sum of the die is equal to the sum that you got on the first roll, you win.\n"
    print "IN BETWEEN: \n In a range of Ace to King, guess a card. If your guess is inbetween two randomly selected cards you win. If it isn't you lose.\n"

def betty(balance):
    validBet = 0
    while validBet == 0:
        print "You have $", balance
        bet = raw_input("Enter a bet: ")
        if bet.isdigit() and int(bet) <= balance:
            bet = int(bet)
            if bet == 666:
                print "Just when you think its over. Your Demons laugh and whisper. /\/\(=-=)/\/\ \n \n \n INSERT TEXT HERE"
            return bet
        else:
            print "That is not a valid bet."

def score(balance):
    os.system("clear")
    valid = True
    while valid:
        choice = raw_input("Do you want to save your balance (1) or discard it (2): ")
        if choice == "1":
            name = raw_input("Enter your name (spaces will be changed to underscores): ")
            A = open("Scores.txt", "r").read()
            A = A.split()
            B = open("Scores.txt", "r").readlines()
            for i in A:
                if i.isdigit():
                    i = int(i)
                else:
                    A.remove(i)
            count = 0
            for i in A:
                A[count] = int(i)
                count += 1
            finalName = ""
            for i in name:
                if i == " ":
                    i = "_"
                finalName += i
            os.system("clear")
            index = 0
            valid = True
            if len(A) > 10:
                rang = 10
            else:
                rang = len(A)
            for j in range(rang):
                if valid:
                    if balance >= A[index]:
                        B.insert(index, str(balance) + " " + finalName + "\n")
                        print "Your balance of", balance, "placed number", j + 1, "on the table. \n"
                        valid = False
                    elif j == 9:
                        print "Your balance of", balance, "was not high enough to get on the table. \n"
                        valid == False
                    else:
                        index += 1
            f = open("Scores.txt", "w")
            for i in B:
                f.write(str(i))
            f.close()
            C = open("Scores.txt", "r").read()
            print "The new top balances are: \n", C
            time.sleep(3)
            valid = False
        elif choice == "2":
            valid = False

def main():
    os.system("clear")
    balance = 1000
    print "Welcome to the Python casino! What would you like to do?"
    choice = ""
    while choice != "5":
        choiceInt = 0
        while choiceInt == 0:
            if balance == 0:
                print "You lost all your money."
                return
            choice = raw_input("\n 1 - Guessing Game \n 2 - Craps \n 3 - In Between \n 4 - Help \n 5 - Quit \n \n Enter 1-5 to choose what you want to do: ")
            if choice.isdigit():
                choiceInt== 1
                if choice == "1":
                    balance = guessingGame(balance)
                elif choice == "2":
                    balance = craps(balance)
                elif choice == "3":
                    balance = inBetween(balance)
                elif choice == "4":
                    directions()
                elif choice == "5":
                    print "Your final balance is", balance
                    score(balance)
                    os.system("clear")
                    return
            else:
                print "That is not a valid choice."

main()
