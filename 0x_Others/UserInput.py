print("Enter your name")
name = input()
print(f"Hello {name}")

### Using prompt inside input() function then taking input in the same line
name = input("Enter your name: ")
print(f"Hello {name}")

# Input number because input() only takes str by default
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
print(f"{num1} + {num2} = {num1+num2}")