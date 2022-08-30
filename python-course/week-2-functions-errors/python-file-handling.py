# opening file and reading contents
file = open("test.txt", mode = 'r')
data = file.readline()
print(data)
file.close()

# opening and closing with the "with" statement
with open("test.txt", mode = "r") as file:
    data = file.readline()
    print(data)

# creating files
with open('newfile.txt', mode="w") as file:
    # writing single lines to a file
    file.write("This is a new file created")

    # writing multiple lines
    file.writelines(["\nThis is a second line", "\nAnd a third line - horray"])

with open('newfile.txt', 'a') as file:
    file.writelines(["\nThis line is appended!", "\nAnd this one, too!"])   

# adding a try except block to catch errors if file does not exist
try:
    with open('newfile.txt', 'a') as file:
        file.writelines(["\nNo Exception raised"])
except FileNotFoundError as e:
    print("Error: ", e)