def d():
    animal = "elephant"
    def e():
        # declare that you will change the "animal" variable
        nonlocal animal
        animal = "giraffe"  
        print("Inside nested function: " + animal)
    
    print("Before calling function: " + animal)
    e()
    print("After nested function: " + animal)

# global variable
animal = "camel"
d()
print("Global animal: " + animal)