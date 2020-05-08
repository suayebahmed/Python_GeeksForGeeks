import random

number = random.randint(1,9)
guess = int(input("Guess a number between 1-9, : "))

if guess == number:
    print("Exactly Right.")
elif guess > number:
    print('Your guessed is way too high')
else:
    print("Your number is way too low.")
