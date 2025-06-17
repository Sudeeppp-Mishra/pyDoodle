# Sort List Alphanumerically - use sort()
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thisNumericList = [10, 50, 42, 12, 44]
thisNumericList.sort()
print(thisNumericList)

# Sort descending - pass argument reverse = True:
thisNumericList.sort(reverse = True)
print(thisNumericList)

# Customize sort function
# we can customize our own function by using the keyword argument key = function - the function will return a number that will be used to sort the list (the lowest number first)
def myfunc(n):
    return abs(n - 50)

thisNumericList.sort(key = myfunc)
print(thisNumericList)

# Case Insensitive Sort - sort() method by default is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# we can use built-in functions as key functionw when sorting a list, so if we want case-insensitive sort functin, use str.lower as a key function
thislist.sort(key = str.lower)
print(thislist)

# Reverse order of list, regardless of the alphabet - use reverse() methdo that reverses the current sorting order of the elements
thislist = ["banana", "Oragne", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)