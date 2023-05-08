## [@] - Flames LLC 20XX - 2023 

python
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y
        return self.result

    def subtract(self, x, y):
        self.result = x - y
        return self.result

    def multiply(self, x, y):
        self.result = x * y
        return self.result

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero.")
        self.result = x / y
        return self.result

    def power(self, x, y):
        self.result = x ** y
        return self.result

    def clear(self):
        self.result = 0
        return self.result


if __name__ == "__main__":
    calculator = Calculator()
    print("Simple Calculator App")
    while True:
        operation = input("Enter operation (+, -, *, /, ^, C to clear, Q to quit): ")
        if operation.lower() == "q":
            break
        elif operation.lower() == "c":
            calculator.clear()
            print("Cleared")
        else:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if operation == "+":
                    print(calculator.add(num1, num2))
                elif operation == "-":
                    print(calculator.subtract(num1, num2))
                elif operation == "*":
                    print(calculator.multiply(num1, num2))
                elif operation == "/":
                    print(calculator.divide(num1, num2))
                elif operation == "^":
                    print(calculator.power(num1, num2))
                else:
                    print("Invalid operation. Please try again.")
            except ValueError:
                print("Invalid input. Please enter numbers.")
            except Exception as e:
                print(f"Error: {e}")
