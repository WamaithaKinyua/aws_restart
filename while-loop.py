# While loop
print("Welcome to Guess the Number!")
print("the rules are simple. I will think of a number, and you will try and guess it.")
import random
number = random.randint(1,10)
isGuessRight = False
while isGuessRight !=True:
    guess = input("Guess a number between 1 and 10?")
    if int(guess) ==number:
        print("You guesses {}. That is correct! You win!".format(guess))
