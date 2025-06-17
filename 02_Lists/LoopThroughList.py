# We can loop through the list items by using a for loop
thislist = ["apple", "banana", "cherry"]
for i in thislist:
    print(i)

print("\n")
# Loop through the index nmbers - we can also loop through the list items by referring to their index number using range() and len()
for i in range(len(thislist)):
    print(thislist[i])
    
print("\n")
# Using a while loop
i = 0
while i< len(thislist):
    print(thislist[i])
    i+=1

print("\n")
# Looping using LIST COMPREHENSION- list comprehension offers the shortest syntax for looping through lists
# A short hand for loop that will print all items in a list:
[print(i) for i in thislist]