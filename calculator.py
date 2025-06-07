ef add(numbers):
    return sum(numbers)

def subtract(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            return "Error: Division by zero is not allowed."
        result /= num
    return result

def calculator():
    print("Multi-Number Calculator")
    print("Operations: + for add, - for subtract, * for multiply, / for divide")
    
    op = input("Enter an operator (+, -, *, /): ")
    num_input = input("Enter numbers separated by space: ")
    
    try:
        numbers = list(map(float, num_input.strip().split()))
        
        if len(numbers) < 2:
            print("Please enter at least two numbers.")
            return

        if op == '+':
            result = add(numbers)
        elif op == '-':
            result = subtract(numbers)
        elif op == '*':
            result = multiply(numbers)
        elif op == '/':
            result = divide(numbers)
        else:
            print("Invalid operator.")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input. Please enter only numeric values.")

#Run the calculator
calculator()