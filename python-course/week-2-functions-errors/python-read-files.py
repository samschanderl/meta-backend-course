# reading the entire file
with open('sample.txt', "r") as file:
    print(file.read())

# reading single line
with open('sample.txt', "r") as file:
    print(file.readline())

# reading multiple lines as a list
with open('sample.txt', "r") as file:
        # I can save the list data and loop over it
        data = file.readlines()
        for x in data:
            print(x)