# Variable is created the moment we first assign a value to it

num = 5
name = "Krishna"

print(num)
print(name)

# Variables do need to be declared with any particulaar type, and can even change type after they have been set

x = 30 # x is of type int
x = "Ram" # x is now of type str
print(x) # Prints Ram

# Casting
# If we want to specify the data type of a variable, this can be done with casting:

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

# NOTE: type() is a built-in function that tells us the type of a value
print(type(x),x) # prints type of x and then value of x
print(type(y),y) 
print(type(z),z)

# for string ".." is same as '..'
p = "Naam"
print(p)
# is same as
p = 'Naam'
print(p)

# Variables names are case-sensitive
a = 4
A = "ram" 
# A will not overwrite a
print(a)
print(A);