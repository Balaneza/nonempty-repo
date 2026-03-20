from calculator import add, subtract, multiply, divide


def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    try:
        a = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ").strip()
        b = float(input("Enter second number: "))

        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        elif op == "/":
            result = divide(a, b)
        else:
            print("Unknown operation")
            return

        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
