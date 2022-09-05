# create a parent class
class Employees:
    def __init__(self, name, last) -> None:
        self.name = name
        self.last = last

# create a child class and add new variables
class Supervisors(Employees):
    def __init__(self, name, last, password) -> None:
        super().__init__(name, last)
        self.password = password

# create a child class and add a new method
class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days?"

adrian = Supervisors("Adrian", "A", "apple")

emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(10))
print(adrian.password)
print(emily.name)