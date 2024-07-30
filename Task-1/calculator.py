def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def main():
    print("Simple Calculator")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input!\n")
        return
    
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = input("Enter choice (1,2,3,4): ")

    if operation == '1':
        print(f"The result is: {add(num1, num2)}")
    elif operation == '2':
        print(f"The result is: {subtract(num1, num2)}")
    elif operation == '3':
        print(f"The result is: {multiply(num1, num2)}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"The result is: {result}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
