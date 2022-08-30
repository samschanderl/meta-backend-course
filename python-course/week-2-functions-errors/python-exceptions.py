def divide_by(a,b):
    return a / b

try:
    ans = divide_by(40 / 0)

    # catch a specific exeption
except ZeroDivisionError as e:
     print(e, "we cannot divide by 0")
     print(e.__class__)

    # catch an unknown exception
except Exception as e:
    print("something went wrong", e)
    print(e.__class__)