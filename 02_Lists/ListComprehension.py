# Offers a shorter syntax when we want to create a new list based on the values of an existing list

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
        
print(newlist)

# with list comprehension above code can be written with only one line of code

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

## SYNTAX
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged


# The condition is option and can be omitted
newlist = [x for x in fruits]
print(newlist)

## ITERABLE
# The iterable can be any iterable object, like list, tuple, set etc.
# eg: we can use the range() function to create an iterable
newlist = [x for x in range(10)]
print(newlist)

## EXPRESSION
# the expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in te new list:
newlist = [x.upper() for x in fruits]
print(newlist)

# we can set the outcome to whaever we like:
newlist = ["hello" for x in fruits]
print(newlist)

# The expression can also contain condition, not like a filter, but as a way to manipulate the outcome
newlist = [x if x!="banana" else "orange" for x in fruits]
print(newlist)