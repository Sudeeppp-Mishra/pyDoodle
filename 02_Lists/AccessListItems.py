thisList = ["apple", "banana", "mango"]
print(thisList[2])

#####################
# Negative Indexing
# Negative indexing means starts from the end -1 refers to the last item, -2 is 2nd last and etc.

print(thisList[-2])

# Range of Indexes
thisList = ["apple", "banana", "orange", "mango", "strawberry", "kiwi"]
print(thisList[2:5]) # start index (2) -> included; end index (5) -> not included
print(thisList[2:])
print(thisList[:4])
print(thisList[-4:-1])

# Check if item exist
if "apple" in thisList:
    print("Yes, 'apple' is in the fruits list")