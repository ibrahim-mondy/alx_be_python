number1 = int(input("Enter the first number:"))
number2 = int(input("Enter the second number:"))

type_of_operation = input("Choose the operation (+, -, *, /):")

match type_of_operation:
    case "+":
        result = number1 + number2
        print(" The result is",result)
    case "-":
        result =  number1 - number2
        print(" The result is",result)
    case "*":
        result =  number1 * number2
        print(" The result is",result)
    case "/":
        print("Cannot divide by zero")
        result =  number1 / number2
        print(" The result is",result)
        