# We already know we can't combine strings and number like:
# age = 30
# txt = "Hello" + age
# print(txt)

####################################################################################
## But we can combine strings and numbers by using f-strings or format() method!!!
####################################################################################

############################
# F-Strings

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
############################

age = 34
txt = f"Hello, I'm {age} years old!"
print(txt)

# {age} so here {} curly braces creates placeholder i.e., we have added place holder for age and a placeholder can contain VARIABLES, OPERATIONS, FUNCTIONS, and MODIFIERS to format the value

# A placeholder can include a modifier to format the value.
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
price = 100
print(f"The price is ${price:.2f}")
print(f"The price with 10% VAT is ${price+price*10/100}")


