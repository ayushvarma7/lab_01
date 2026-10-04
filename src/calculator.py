def add(a, b):
    return a + b


def fun1(a, b):
    return a + b


def subtract(a, b):
    return a - b


def fun2(a, b):
    return a - b


def multiply(a, b):
    return a * b


def fun3(a, b):
    return a * b


def fun4(x, y, z):
    return x + y + z


def fun5(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero.")
    return a % b


def fun6(a, b):
    return a ** b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return a ** b


def calculator(operation, a, b):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "**": power,
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    return operations[operation](a, b)


if __name__ == "__main__":
    print("Simple Calculator")
    print("Operations: +, -, *, /, **")

    while True:
        user_input = input("Enter expression (e.g. 5 + 3) or 'q' to quit: ").strip()

        if user_input.lower() in {"q", "quit", "exit"}:
            print("Goodbye!")
            break

        try:
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError("Use format: number operator number")

            a = float(parts[0])
            operation = parts[1]
            b = float(parts[2])

            result = calculator(operation, a, b)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
