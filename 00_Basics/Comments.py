# Comments in python starts '#', and Python will render the rest of the line as comment
# Purpose of comment for in-code documentation
# This is a comment

print("Hi") # Prints Hi

# Multiline Comments
# Python does not really have a syntax for multiline comments.

# To add a multiline comment you could insert a # for each line

# or, if we include something inside triple quotes - we can either use """...""" or '''...''' to write a string that spans multiple lines
# it's not actually multi line comment but it acts like a multi-line comment coz it won't affect your program
# But technically """...""" is a multi-line string literal, if you assign it to a variable or use it, it's a string
# If you don't use it, python will treat it as a comment and will ignore it

# ACTUALLY TRIPLE QUOTES ARE USED LIKE THIS:
message = """Hiiii
This is a multi-line string
in Python..."""
print(message)

"""
It can be taken as comment as it is not assinged to any variable
"""