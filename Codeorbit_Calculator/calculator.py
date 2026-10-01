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


