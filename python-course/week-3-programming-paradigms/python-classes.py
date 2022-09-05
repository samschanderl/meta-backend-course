# creating and instantiating an empty class
class EmptyClass:
    pass # role of a placeholder if nothing is done with it

empty_class = EmptyClass()

# create a simple class
class MyClass:
    a = 5

    def hello(self):
        print("Hello there")

myclass = MyClass()
print(myclass.a)
print(myclass.hello())