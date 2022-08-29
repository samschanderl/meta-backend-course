# loop over a string
str = "Looping"

for item in str:
	print(item)

# for loop - looping over list
favorites = ["cake", "cookies", "ice cream", "croissant", "Tiramisu"]

for item in favorites:
	print("I like " + item)

# for loop - with index and enumerate
for idx, item in enumerate(favorites):
	print(idx, item)

# while loop - looping over list
count = 0

while count < len(favorites):
	print("I like " + favorites[count]
	count += 1
