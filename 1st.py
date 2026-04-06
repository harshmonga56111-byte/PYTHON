# Simple Calculator without functions

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if choice == '1':
    result = x + y
    print("Result:", result)
elif choice == '2':
    result = x - y
    print("Result:", result)
elif choice == '3':
    result = x * y
    print("Result:", result)
elif choice == '4':
    if y != 0:
        result = x / y
        print("Result:", result)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid input")