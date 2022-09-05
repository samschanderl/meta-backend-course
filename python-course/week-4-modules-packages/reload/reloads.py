import importlib
import filechanges

def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_contents
    except:
        pass

# load the function several times
for i in range(5):
    changes()
    input("Hit enter to reload... ")