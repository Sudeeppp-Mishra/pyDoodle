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

