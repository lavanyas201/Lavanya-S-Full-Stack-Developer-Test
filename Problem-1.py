# Problem-1.py

class Calculator:
    def _init_(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'addition' or self.operation == 'add' or self.operation == '+':
            return self.a + self.b
        elif self.operation == 'subtraction' or self.operation == 'subtract' or self.operation == '-':
            return self.a - self.b
        elif self.operation == 'multiplication' or self.operation == 'multiply' or self.operation == '*':
            return self.a * self.b
        elif self.operation == 'division' or self.operation == 'divide' or self.operation == '/':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

# Example usage
if _name_ == "_main_":
    calc = Calculator(10.5, 2.0, "division")
    print(calc.calculate())  # Output: 5.25
