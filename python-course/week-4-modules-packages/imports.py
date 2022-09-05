# importing the full math module
import math

print("Importing the math module")

root = math.sqrt(9)
print(root)

# importing only part of a module
from math import sqrt

root2 = sqrt(16)
print(root2)

# importing a module with an abbreviation
import math as m

cosine = m.cos(0)
print(cosine)


# importing a part of a module and abbreviating it
from math import factorial as f

factorial_10 = f(10)
print(factorial_10)

# importing multiple parts of a module
from math import factorial, log10

x = log10(50)
print(x)

# importing all parts of a module - not best practice because it can get confusing with large projects
from math import *