# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

newList = ["apple", "banana", "mango"]
print(newList)

# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:
duplicateList = ["aa", "aa", "banana", "banana", "apple", "banana"]
print(duplicateList)

print("\n")

########################################
# List Lenght - len() function is used
########################################
print(len(newList))
print(len(duplicateList))

# List can be of any data type:
list1 = ["aa", "bb", "Cc"]
list2 = [1, 4, 4]
list3 = [True, False, True]
print(list1, list2, list3)

print("\n")
# List can contain different data types:
list4 = ["abc", 34, True, 13, "male"]
print(list)

print("\n")
# it is also possible to use list() constructor while creating a new list
list5 = list(("apple", "banana")) # use two round brackets
print(list5)

##############################################################################################################
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
##############################################################################################################