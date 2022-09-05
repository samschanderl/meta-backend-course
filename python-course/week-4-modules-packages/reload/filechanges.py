import os

# list the contents of a given directory
def print_contents():
    contents = os.listdir('/Users/samuelschanderl/dev/learning/meta-backend-course/python-course/week-4-modules-packages/reload')
    print("Current directory contents:")
    print(contents)