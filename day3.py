import random

# generate random number between 1 and 10
secret_number = random.randint(1, 10)

print("Guess a number between 1 and 10")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You guessed it in", attempts, "attempts.")
        break
