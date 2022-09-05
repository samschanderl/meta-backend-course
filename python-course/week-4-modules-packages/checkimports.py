# import other python file
import sample

# built in module
import json

# using the sys module to import new modules
import sys

# tell Python to look for modules in a new directory
sys.path.insert(1, r'/Users/samuelschanderl/dev/learning/meta-backend-course/python-course/week-4-modules-packages/workplace/trial.py')

import trial

print(trial.names)