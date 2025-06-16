# Variables that are created outside of a function are known as global variabls
# Global variables can be used by everyone, both inside of functions and outside

x = "Cool" # Outside myfunc() but it is global so it can be accessed by myfunc()
def myfunc():
    print("He is "+x)

myfunc()

print("\n") # \n is escape character for new line
# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

y = "Hi"
def newfunc():
    y = "Hello"
    print(y) # local variable value
    
newfunc()
print(y) # Global variable value

print("\n")
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

def func1():
    global z
    z = "Heheee" # can't do global z = "Heheee" at first we need to declare it is global and then only we can assing value to it
    print(z)
    
func1()
print(z)

print("\n")
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
p = "Ufff"
def func2():
    global p
    p = "offo"

func2()
print(p)