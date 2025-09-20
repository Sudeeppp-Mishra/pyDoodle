# Slicing
# We can return a range of characters by using the slice syntax
# Specify the start index and the end index, separated by a colon, to return a part of the string

b = "Hello"
print(b[2:5])

# Slice from the start
print(b[:3])

#Slice to the end
print(b[1:])

############################
# Negative Indexing
############################
# Use negative indexes to start the slice from the end of the string:

# ex:
# "Hello": here `o` is in -1 index from back and `e` is in -4
print(b[-4:-1]) # but it don't include -1 index i.e., includes From(-4) index but not included To(-1) index
print(b[-3:-2])