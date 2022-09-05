my_list = [1, 2, 3]

# not a pure function
def add_to_list(item):
    return my_list.appent(item)

# pure function
def add_to_list2(lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list2(my_list, 4)

print(my_list)
print(new_list)