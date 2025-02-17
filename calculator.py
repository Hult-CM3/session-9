def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 // n2

def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))
    print("x * y =", multiply(x, y))
    print("x / y =", divide(x, y))

if __name__ == "__main__":
    main()