# There are built-in methods that we can use on strings

txt = "   Hello, World!"

# Upper Case
print(txt.upper())

# Lower Case
print(txt.lower())

# Remove Whitespace
print(txt.strip())

# Replace String
print(txt.replace("H", "J"))

# Split String - split() method returns a list where the text between the specified separator becomes the list items
print(txt.split(","))