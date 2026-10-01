print("====== Simple calculator ======")

while True:
    try:
        num1 =float(input("enter first number"))
        operator =m input ("enter operator ( + , - , * , / ):")
        num2 =float(input("enter second number"))


        if operator =="+":
            print("Result : ", num1+num2)
        elif operator =="-":
            print("Result : ", num1-num2)
        elif operator == "*":
            print("Result:", num1 * num2)
        elif operator == "/":
            print("Result:", num1 / num2)
        else:
            print("Invalid operator!")

    except ZeroDivisionError:
        # Runs when you divide by 0
        print("Error: You cannot divide by zero!")

    except ValueError:
        # Runs when you type letters instead of a number
        print("Error: Please enter numbers only!")

    # Ask if the user wants to continue
    again = input("Calculate again? (yes/no): ")
    if again != "yes":
        print("Goodbye!")
        break






   
