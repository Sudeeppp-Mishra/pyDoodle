# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Setting the data type
# In python, type is set when we assign a value to a variable

x = "Hello" # str
print("Type:",type(x),"\nValue:",x,"\n")

x = 20 # int
print("Type:",type(x),"\nValue:",x,"\n")

x = 20.5 # float
print("Type:",type(x),"\nValue:",x,"\n")

x = 1j # complex
print("Type:",type(x),"\nValue:",x,"\n")

x = ["apple", "banana", "mango"] # list
print("Type:",type(x),"\nValue:",x,"\n")

x = ("apple", "banana", "mango") # tuple
print("Type:",type(x),"\nValue:",x,"\n")

x = range(6) # range
print("Type:",type(x),"\nValue Range:",x, "Values:",x[0], x[1], x[2], x[3], x[4], x[5],  "\n")

x = {"name": "John", "age": 32} # dict
print("Type:",type(x),"\nValue:",x,"\n")

x = frozenset({"apple", "banana", "cherry"})
print("Type:",type(x),"\nValue:",x,"\n")

x = True # bool
print("Type:",type(x),"\nValue:",x,"\n")

x = b"Hello" #bytes
print("Type:",type(x),"\nValue:",x,"\n")

#########################################
# Setting the specific data type
#########################################

x = str("Hello World")
print("Type:",type(x),"\nValue:",x,"\n")

x = complex(2j)
print("Type:",type(x),"\nValue:",x,"\n")

x = list(("apple", "banana", "mango"))
print("Type:",type(x),"\nValue:",x,"\n")

x = dict(name="John", age=23)
print("Type:",type(x),"\nValue:",x,"\n")