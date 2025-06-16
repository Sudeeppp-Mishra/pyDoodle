# Many value to multiple variables

x, y, z = "Hi", "Hello", "Bye"
print(x)
print(y)
print(z)

# One Value to Multiple Variables

x = y = z = "Wooooooooooaaahhhhh"
print(x)
print(y)
print(z)

# Unpacking a Collection
# If we have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["Mango", "Strawberry", "Apple"]
x, y, z = fruits
print(x)
print(y)
print(z)

# We can use comma to ouput multiple variables in print() function
print(x, y, z)
# or we can use + operator to output multiple variables
print(x + y + z) # But it won't auto add spaces between variables

# But if we try to combine a string and a number with + operator in print function it's an error
# x = 5
# y = "Ram"
# print(x+y) # ERROR
# So best way is to use coma, which even supports different data types
x = 5
y = "Ram"
print(x, y)