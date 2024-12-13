def performOperation(numberOne, numberTwo, operation):
    if operation == "+":
        return numberOne + numberTwo
    elif operation == "-":
        return numberOne - numberTwo
    elif operation == "*":
        return numberOne * numberTwo
    elif operation == "/":
        if numberTwo != 0:
            return numberOne / numberTwo
        else:
            return "Error (division by zero)"
    else:
        return "Invalid operator"

def main():
    numberOne = int(input("Enter the first number: "))
    numberTwo = int(input("Enter the second number: "))
    operation = input("Enter an operator (+ - * /): ").strip()
    
    result = performOperation(numberOne, numberTwo, operation)
    
    if result == "Invalid operator":
        print("Error: Invalid operator. Please use +, -, *, or /.")
    elif result == "Error (division by zero)":
        print("Error: Cannot divide by zero.")
    else:
        print(f"{numberOne} {operation} {numberTwo} = {result}")

main()
