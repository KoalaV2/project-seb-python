import math
import subprocess 
def calculator():
    subprocess.call(["espeak", "Please etner the first number"])
    first_number = float(input("Please enter the first number: "))
    subprocess.call(["espeak", "What operation shall be used?"])
    operation = input("What operation shall be used? :")
    subprocess.call(["espeak", "Please enter the second number"])
    second_number = float(input("Please enter the second number: "))


    if operation == "+" or operation == "add":
        result = first_number + second_number
        operand = "+"
    elif operation == "-" or operation == "subtract":
        result = first_number - second_number
        operand = "-"
    elif operation == "*" or operation == "multiply":
        result = first_number * second_number
        operand = "*"
    elif operation == "/" or operation == "divide":
        result = first_number / second_number
        operand = "/"
    elif operation == "pow" or operation == "power":
        result = first_number ** second_number
        operand = "to the power of"
    else:
        print("Operation not recognized, exiting to main menu...")
        return
    print("\n{} {} {} is {}".format(first_number, operand, second_number, result))
