# Remove Specified Item - remove() method
thislist = ["apple", "banana", "mango"]
thislist.remove("banana")
print(thislist)

# if there are more than one item with the specified value, the remove() method removes the first occurence
thislist = ["apple", "banana", "kiwi", "banana"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index - pop() method
thislist = ["apple", "banana", "mango"]
thislist.pop(1)
print(thislist)

# if we don't specify the index, the pop() method removes the last item
thislist = ["apple", "banana", "mango"]
thislist.pop()
print(thislist)

# del keyword also removes the specified index
del thislist[0]
print(thislist)
# del keyword can also delete the list completely
thislist = ["apple", "banana", "mango"]
del thislist
# print(thislist) # can't do this as del thislist completely deleted the variable thislist from memory i.e., it no longer exists

# Clear the List - clear() method empties the list, the list still remains, but with no content
thislist = ["apple", "banana", "mango"]
thislist.clear()
print(thislist)