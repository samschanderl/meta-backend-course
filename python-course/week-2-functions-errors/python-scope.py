#global scope
my_global = 10

def fn1():

    # enclosed scope
    enclosed_v = 8

    def fn2():
        # local scope
        local_v = 5
        print("Access to global: - ", my_global)
        print("Access to enclosed: - ", enclosed_v)
    fn2()

fn1()