###public, private and protected variables
"""
Public variable: any variable defined by a casual name in any class are public variable
if the modules are imported then the variables of classes of that module can be accessed
these are public variables

protected variables: any variables that can be accessed by the class itself and the offspring
class of that class(another Class inherited from that class)

private variables: Cant even be used inside the class. Ac special way to access private variables

"""

class Employees:
    __privat = 1000
    workdays_per_month = 22
    var = 1
    var1 = 4
    var2 = 6

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return (f"The name is : {self.name}, salary is :{self.salary} and the role is : {self.role}")

    @classmethod
    def changeleaves(cls, new_workdays):
        cls.no_of_new_workdays = new_workdays


    @classmethod
    def from_str(cls, string):
    #     params = string.split("-")
    #     return cls(params[0], int(params[1]),params[2])
    #one liner
        return cls(*string.split("-"))

class Player:
    _protected_variable = 10
    var = 2
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def print_details(self):
        return f"The name is {self.name}. Game is {self.game}"


class Programmer_Employee_Player(Employees, Player):
    var = 3
    var1 = 5


ranjan = Employees("Ranjan", 3212, {"Tutor"})
lamsal = Employees("lamsal", 3212112, {"Inern"})

shyaam = Player("Shyaam", ["Cricket"])

print(shyaam._protected_variable) #this is protected variable

al_in_one = Programmer_Employee_Player("all", 2121, "one")
print(al_in_one._protected_variable)
#can be accessed through offspring class


"""Noe to acessed the private variable at employee class we need to write the name
of the variable along with the name of class
variable saved as : __varname
variable should be called as object._Classname__varname
"""

print(ranjan._Employees__privat)

