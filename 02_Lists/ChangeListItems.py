# Change item value
thisList = ["apple", "banana", "mango"]
thisList[1] = "strawberry"
print(thisList)

# Change a Range of Item Values
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thisList[1:3] = ["blackberry", "watermelon"]
print(thisList)
thisList[1:2] = ["strawberry", "dragonFruit"] # if we insert more items than we replace, the new items will be inserted where we specified, and the remaining items will move accordingly
print(thisList)

thisList = ["apple", "banana", "mango"]
thisList[1:3] = ["watermelon"] # if we insert less items than we replace, the new items will be inserted where we specified, and the remaining items will move accordingly
print(thisList)

# Insert Items
# to insert new list item, without replacing any of the existing values, we can use the insert() method which inserts an item at the specified index
thisList = ["apple", "banana", "mango"]
thisList.insert(2,"strawberry")
print(thisList)