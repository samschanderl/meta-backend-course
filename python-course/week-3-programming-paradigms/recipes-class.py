from copyreg import dispatch_table


class Recipe():
    def __init__(self, dish, items, time) -> None:
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has " + str(self.items) + " and takes " + str(self.time) + " min to prepare")

pizza = Recipe("Pizza", ["cheese", "bread", "tomato"], 45)
pasta = Recipe("Pasta", ["mozzarella", "pasta", "tomato"], 15)

print(pizza.contents())
print(pasta.contents())