import random

print("===== NUMBER GUESSING GAME =====")

while True:
    # Computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI am thinking of a number between 1 and 100.")
