num_one = float(input("Enter first number: "))
num_two = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(f"Result = {num_one + num_two}")
elif operator == "-":
    print(f"Result = {num_one - num_two}")
elif operator == "*":
    print(f"Result = {num_one * num_two}")
elif operator == "/":
    # Check for division by zero
    if num_two != 0:
        print(f"Result = {num_one / num_two}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator.")
