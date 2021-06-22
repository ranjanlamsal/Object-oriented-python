"""
A class method is a method that is bound to a class rather than its object.
It doesn't require creation of a class instance, much like staticmethod.

The difference between a static method and a class method is:

Static method knows nothing about the class and just deals with the parameters
Class method works with the class since its parameter is always the class itself.

Class method can be called by both object and class

"""

class Employees:
    workdays_per_month = 22

    @classmethod
    def printer(cls, new_workdays):
        """
        instead of self we got cls. Cls is that class whose instance is the
        instance that has called this function
        """
        cls.no_of_new_workdays = new_workdays

ranjan = Employees()

ranjan.printer(34)
'''
Now this changes the class variable workdays_per_month
'''
print(ranjan.no_of_new_workdays)
Employees.printer(35)
print(ranjan.no_of_new_workdays)






