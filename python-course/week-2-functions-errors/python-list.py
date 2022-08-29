list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e","f"]
list3 = ["hello", 1, True, 40.22]
# nested lists
list4 = [1, [1,2,3], 2, 3]

# get the third item inside list 1
print(list1[2])

# print entire list using *
print(*list1)

# insert items using the insert() function - specify index
list1.insert(len(list1), 6)
print(list1, sep=" ")

# insert items using append() function - added to the end of the list
list1.append(7)
print(list1, sep=" ")

# insert multiple items using extend()
list1.extend([8,9,10])
print(list1, sep=" ")

#remove items using pop() method - giving index
list1.pop(len(list1)-1)
print(list1, sep=" ")

# remote items using del - specify index
del(list1[2])
print(list1, sep=" ")

# iterate over list
for x in list1:
    print("value: ", x)