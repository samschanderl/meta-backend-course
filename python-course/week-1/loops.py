import time
start_time = time.time()

# outer loop
for i in range(10):
	#inner loop
	for j in range(10):
		print(j, end=" ")
	print()

# print the time needed
print("time needed: ", round((time.time() - start_time), 2))