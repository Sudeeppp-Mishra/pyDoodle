# We cannot copy a list simply by list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2
# use copy() method to copy list
list1 = ["hello", "hi"]
list2 = list1 # list2 is not a new list, it just points to the same object as list1
print(list2)
list1.append("hehe")
print(list2)
list1 = ["hello", "hi", "bye"] # reassining create new object but list2 is still pointing to previous original one
print(list2)


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# using list() method
mylist1 = list(mylist)
print(mylist)

# use the slice operator
# we can also make a copy of a list by using the : (slice) operator
thislist1 = ["C", "C++", "Java"]
mylist1 = thislist1[:]
print(mylist1)