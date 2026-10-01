import random

print("===== NUMBER GUESSING GAME =====")

while True:
    # Computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI am thinking of a number between 1 and 100.")

     while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a number only!")
            continue

        attempts = attempts + 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Correct! You guessed it in", attempts, "attempts.")
            break
