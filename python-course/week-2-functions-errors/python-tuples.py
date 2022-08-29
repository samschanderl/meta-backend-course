my_tuple = (1, "strings", 4.5, True)

# get values with index value
print(my_tuple[1])

# get type of tuple
print(type(my_tuple))

# get the number of occurances inside a tuple
print(my_tuple.count("strings"))

# get the index of a value
print("4.5 at index: ", my_tuple.index(4.5))

# iterate over tuples
for x in my_tuple:
    print(x)

# tuples are immutable - will return type error
my_tuple[0] = 5 