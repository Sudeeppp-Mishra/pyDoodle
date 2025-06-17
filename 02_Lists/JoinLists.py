# using + operator to concatenate or join two or more lists
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# another way is to append all the items from list2 into list1, one by one
list1 = ['d', 'e', 'f']
list2 = [4, 5, 6]
for i in list2:
    list1.append(i)
    
print(list1)

# or we can use the extend() method, where the purpose is to add elements from one list to another list
list1 = ['g', 'h', 'i']
list2 = [7, 8, 9]
list1.extend(list2)
print(list1)