print("Enter your name")
name = input() # Python stops executing when it comes to the input() function, and continues when the user has given some input.
print(f"Hello {name}")

### Using prompt inside input() function then taking input in the same line
name = input("Enter your name: ")
print(f"Hello {name}")

# Input number because input() only takes str by default
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
print(f"{num1} + {num2} = {num1+num2}")


# Validate Input

# It is a good practice to validate any input from the use. In example above,
# an error will occur if the user inputs something other tahn a number.else
# To avoid getting an erro, we can test the input, and if it is not a number, the user could get a message
# like "Wrong input, please try again", and allowed to make a nuew input:

y = True

while y == True:
    x = input("Enter a number: ")
    try:
        x = float(x)
        y = False
    except:
        print("Wrong input, please try again.")
        
print("Thank You!")