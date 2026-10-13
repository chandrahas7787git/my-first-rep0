while True:
    print("\n--- Calculator ---")
    num1 = float(input("First number (or type 0 to exit): "))
    if num1 == 0:
        break
    op = input("Operator (+ - * /): ")
    num2 = float(input("Second number: "))

    if op == "+": print(f"Result = {num1 + num2}")
    elif op == "-": print(f"Result = {num1 - num2}")
    elif op == "*": print(f"Result = {num1 * num2}")
    elif op == "/": 
        print("Can't divide by zero!" if num2 == 0 else f"Result = {num1 / num2}")
    else: print("Wrong operator!")

print("Bye! Calculator closed.")