import sys

def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

def multiply(a, b):
    result = a * b
    return result

def divide(a, b):
    result = a / b
    return result

print("Welcome to the digital calculator!\n")

operationList = ["add", "subtract", "multiply", "divide"]
for index, item in enumerate(operationList, 1):
    print(f"{index}. {item}") 
operator = int(input("\nWhich operation would you like to perform (1-4): "))

choice_num = int(operator)
if 1 <= operator <= len(operationList):
    selected_option = operationList[choice_num-1]
else:
    print("\nSelected option not on displayed list.")
    sys.exit()



operand1 = float(input("\nPlease input the first number of the equation: "))
operand2 = float(input("\nPlease input the second number of the equation: "))

if selected_option == "add":
    answer = add(operand1, operand2)
    print(f"{operand1:.1f} + {operand2:.1f} = {answer:.1f}")

elif selected_option == "subtract":
    answer = subtract(operand1 , operand2)
    print(f"{operand1:.1f} - {operand2:.1f} = {answer:.1f}")

elif selected_option == "multiply":
    answer = multiply(operand1, operand2)
    print(f"{operand1:.1f} x {operand2:.1f} = {answer:.1f}")

elif selected_option == "divide":
    answer = divide(operand1, operand2)
    print(f"{operand1:.1f} / {operand2:.1f} = {answer:.1f}")

else:
    print("Invalid operator")