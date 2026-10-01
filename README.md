# CodeOrbit Python Programming Internship

Python tasks completed for the CodeOrbit Tech Python Programming Internship (1 Month, 3 Tasks).

## Tasks
1. Simple Calculator
2. To-Do List CLI App
3. Number Guessing Game

## How to run
Open a terminal in the task folder and run the file with Python, for example: `python calculator.py`

---

## Task 1: Simple Calculator

A command-line calculator that takes input from the user.

Features:
- Addition, subtraction, multiplication and division
- Handles division by zero and invalid input using try/except
- Repeats until the user quits

Sample Input/Output:

    ===== SIMPLE CALCULATOR =====
    Enter first number: 10
    Enter operator (+, -, *, /): +
    Enter second number: 5
    Result: 15.0
    Calculate again? (yes/no): yes
    Enter first number: 10
    Enter operator (+, -, *, /): /
    Enter second number: 0
    Error: You cannot divide by zero!
    Calculate again? (yes/no): no
    Goodbye!

---

## Task 2: To-Do List CLI App

A command-line to-do list app.

Features:
- Add, view and remove tasks
- Tasks stored in a list while the program runs
- Tasks saved to tasks.txt on exit
- Each feature is a separate function

Sample Input/Output:

    ===== TO-DO LIST =====
    1. Add task
    2. View tasks
    3. Remove task
    4. Save and exit
    Enter your choice (1-4): 1
    Enter the task: Study Python
    Task added!
    Enter your choice (1-4): 2
    Your tasks:
    1 . Study Python
    Enter your choice (1-4): 3
    Enter the task number to remove: 1
    Task removed!
    Enter your choice (1-4): 4
    Tasks saved to tasks.txt. Goodbye!

---

## Task 3: Number Guessing Game

The computer picks a random number between 1 and 100 and the user guesses it.

Features:
- "Too high" / "Too low" hints after each guess
- Counts and shows the number of attempts
- Multiple rounds using a loop

Sample Input/Output:

    ===== NUMBER GUESSING GAME =====
    I am thinking of a number between 1 and 100.
    Enter your guess: 50
    Too low! Try again.
    Enter your guess: 75
    Too high! Try again.
    Enter your guess: 62
    Correct! You guessed it in 3 attempts.

    Play again? (yes/no): no
    Thanks for playing! Goodbye!

---

Made by Jhansi Veni | GitHub: Jhansiveni
