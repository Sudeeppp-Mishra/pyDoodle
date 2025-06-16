# Appending items - adding at the end of the list
thisList = ["apple", "banana", "strawberry"]
thisList.append("orange")
print(thisList)

# Insert Items
# to insert new list item, without replacing any of the existing values, we can use the insert() method which inserts an item at the specified index
thisList = ["apple", "banana", "mango"]
thisList.insert(2,"blueberries")
print(thisList)

# Extend List - to append elements from another list to the current list
thisList = ["apple", "banana", "strawberry"]
tropical = ["mango", "pineapple", "papaya"]
thisList.extend(tropical)
print(thisList)

# Add any iterable
# extend() method does not have to append lists, we can add any iterable object (tuples, sets, dictionaries etc.)
thisList = ["apple", "banana", "strawberry"]
thisTupel = ("kiwi", "orange")
thisList.extend(thisTupel)
print(thisList)