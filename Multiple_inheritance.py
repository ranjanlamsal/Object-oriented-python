class Employees:
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

#ram = Programmer_Employee_Playe()
"""iT SHOWS error:
TypeError: __init__() missing 3 required positional arguments: 'aname', 'asalary', and 'arole'
this is because as we inherit the class the constructor is also inherited.
and thus the required arguments must be passed to the object to create it
In case of multiple inheritance,the constructor is used of the 
first parent class that is inherited while creating the ofspring class
if no constructor in 1st parent then 2nd parent is searched for the constructor

"""

ram = Programmer_Employee_Player("Ram", 1001010, "Programmer")

print(ram.printdetails())
"""The attribute of Employee class printdetails"""

# print(ram.print_details())
"""The attribute of player class.
But this shows error since the print_details attribute takes argument name and 
games. But while creating the object ram, we only passed name, salary and role 
as the constructor used is of class Employee"""

ram.game = ["Football", "Hockey"]
"""Now we have declared the object variable game
Now print_details() runs smoothly as the req arguments are passed"""

print(ram.print_details())


"""There is a variable named var in all three classes."""
print(ram.var)
"""gives 3 as the variable is first looked in the self class and
if found then the value is assigned as of self class"""

print(ram.var1)
"""gives 5 as the var1= 5 in first parent (Employees)."""

print(ram.var2)
"""gives 6 as var2 = 6 in second parent (Playes)"""

"""
So we can conclude that any attributes or variables are first searched in the self
class, if found then variable and attributes (same) in any other class is overridden
Then it is looked into the first parent and finally to second parent and so on
"""