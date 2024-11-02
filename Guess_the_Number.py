import random

print("Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

number = random.randint(1, 100)
guess = int(input("Enter your guess: "))

while guess != number:
    if guess < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
    guess = int(input("Enter your guess: "))

print("Congratulations! You guessed the number correctly!") 
