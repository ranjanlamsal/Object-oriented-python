"""
Static methods, much like class methods, are methods that are bound to a
class rather than its object.

They do not require a class instance creation. So, they are not dependent
 on the state of the object

Static methods have a limited use case because, like class methods or any other
 methods within a class, they cannot access the properties of the class itself.

However, when you need a utility function that doesn't access any properties of
a class but makes sense that it belongs to the class, we use static functions.

"""

class Employees:
    workdays_per_month = 22

    def __init__(self, aname, asalary, arole):
        """This is a constructor. It is used to construct objects of class
        here self means the object that is constructed uing this constructor
        aname, asalary, arole are the arguments taken"""

        self.name = aname
        self.salary = asalary
        self.role = arole

    @staticmethod
    def printdetails(strings):
        print("THis function does nothing but print "+ strings)
        return 0

ranjan = Employees("Ranjan",30030303,"TUtor")
ranjan.printdetails("I am awesome")
