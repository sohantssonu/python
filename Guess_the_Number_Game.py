import random

random_number = random.randint(1, 100)

user_guess = int(input("Guess the number: "))

while user_guess != random_number:
    if user_guess > random_number:
        print("Too high! Guess lower.")
    else:
        print("Too low! Guess higher.")
        
    user_guess = int(input("Guess again: "))

print("Congratulations! You guessed the correct number.")
