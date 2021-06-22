class Employees:
    workdays_per_month = 22

    def __init__(self, aname, asalary, arole):
        """This is a constructor. It is used to construct objects of class
        here self means the object that is constructed uing this constructor
        aname, asalary, arole are the arguments taken"""

        self.name = aname
        self.salary = asalary
        self.role = arole

    @classmethod
    def printer(cls, new_workdays):
        """
        instead of self we got cls. Cls is that class whose instance is the
        instance that has called this function
        """
        cls.no_of_new_workdays = new_workdays


    ####class methods as alternative constructors

    @classmethod
    def from_str(cls, string):
    #     params = string.split("-")
    #     return cls(params[0], int(params[1]),params[2])
    #one liner
        return cls(*string.split("-"))


ranjannn = Employees.from_str("Ranjan-10000-tutor")
"""
So basically we have defined a function (class method ) that takes first argument
as the same class that as called the function. and second argument is a string that 
contains name, salary and role of the object separated by "-".
now the string are splited from "-" so we get the parameters: name salary and role
now te stree splited contents are passed in the class as the return value
so as a return value a new class object is created
"""

print(ranjannn.name)