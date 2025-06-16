# String are surrounded by single or double quotation marks

print("Hello")
# is same as 
print('Hello')

print("\n")

############################
## Quotes inside Quotes
############################
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("Didn't wanna go there")
print("It's 'meee' ")
print('Hello, "Python" ')

print("\n")
# assigning string to variable
a = "this"
print(a)

print("\n")
############################
# Multiline Strings
############################
# Triple quotation is used
a = """This is 
Multi line
String""" # or we can use triple single quotes as well
print(a) # NOTE: in the result, the line breaks are inserted at the same position as in the code

print("\n")
#######################
# STRINGS ARE ARRAYS
#######################
arrayString = "Py th on"
print("0th index character:", arrayString[0])
print("2nd index character: ", arrayString[2])

print("\n")
############################
# Looping Through a String
############################
for x in "Krishna":
    print(x)
    
print("\n")
############################
# String length
############################
# len() function is used
a = "Hiii"
print(len(a))

print("\n")
####################################
# Check character present in string
####################################
# use the keyword 'in'

txt = "this is the best place"
print("place" in txt) # returns True if present in the string else False
print("z" in txt) 
# better for showing msg as well using if
if "is" in txt:
    print("Yes, 'is' is present!")
    
print("\n")
#########################################################################################
# Check if a certain phrase or character is NOT present in string, use keyword 'not in'
#########################################################################################
print("example" not in txt)
if "true" not in txt:
    print("No, 'true' is NOT present")