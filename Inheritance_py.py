"""
In object-oriented programming, inheritance is the mechanism of basing
an object or class upon another object (prototype-based inheritance) or
class (class-based inheritance), retaining similar implementation. ...
An inherited class is called a subclass of its parent class or super class.

"""
class Employees:
    workdays_per_month = 22

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

###SIngle inheritance
"""One class inherited from one class"""
class Programmer(Employees):
    """
    now the programmer class has inherited everything (class veriables,
     attributes and methods from class Employees)
    """
    no_of_holidays = 11

    def __init__(self, aname, asalary, arole, alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = alanguages

        """
        Here we have created a new constructor for this class
        so the constructor of parent class is not used while creating the objects
        
        """

    def print_prog(self):
        return f"The programmer's name is {self.name}.\n" \
               f"The salary is {self.salary}\n" \
               f"The role is {self.role}\n" \
               f"The languages are {self.languages}\n"


ranjan = Employees("ranjan","40000","Coder")
rohan = Employees("Rohan", "30232", "Instructor")

lamsal = Programmer("lamsal", 32321, "Programmer", ["Python", "CPP"])
karan = Programmer("karan", 2112, "Programmer", ["JS"])

print(lamsal.print_prog()) #from programmer class
print(lamsal.printdetails()) #from employee class

print(karan.workdays_per_month) #from employee class
print(karan.no_of_holidays) #from programmer class


