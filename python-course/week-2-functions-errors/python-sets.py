# sets cannot have multiple values

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(set_a)

# add values to the set
set_a.add(6)
print(set_a)

#remove values using remove
set_a.remove(4)
print(set_a)

#remove values using discard
set_a.discard(1)
print(set_a)

# join two sets using union() or |
print("Joint set: ", set_a.union(set_b))
print("Joint set: ", set_a | set_b)

# return the matching items of two sets using intersection() or &
print("Shows matching items: ", set_a.intersection(set_b))
print("Shows matching items: ", set_a & set_b)

# get the set difference to another set (unique items)
print("Only items in set a: ", set_a.difference(set_b))
print("Only items in set a: ", set_a - set_b)

# symmetrical difference - present in either set but not in both sets
print("Present in either set (but not both): ", set_a.symmetric_difference(set_b))
print("Present in either set (but not both): ", set_a ^ set_b)
