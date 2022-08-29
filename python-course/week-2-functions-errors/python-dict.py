sample_dict = {1: "Coffee", 2: "Tea", 3: "Juice", 4: "Beer"}
print(sample_dict[1])

# change value based on key
sample_dict[2] = "Mint Tea"
print(sample_dict)

# delete item based on key
del sample_dict[3]
print(sample_dict)

#iterate over dictionaries
my_d = {1: "Test", "Name": "Jim", "Age": 23, "is_smart": True}
print(my_d)

# add value based on key
my_d[2] = "Test 2"
print(my_d)

#iterate over dictionaries - prints keys
for x in my_d:
    print(x)

#iterate over dictionaries using items() function
for key, value in my_d.items():
    print(str(key), ": ", value)

