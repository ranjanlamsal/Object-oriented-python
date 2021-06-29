'''
str() and repr() both are used to get a string representation of object.

***str() is used for creating output for end user while repr() is mainly used
for debugging and development.
repr’s goal is to be unambiguous and str’s is to be readable.
For example, if we suspect a float has a small rounding error,
repr will show us while str may not.

**repr() compute the “official” string representation of an object
 (a representation that has all information about the object) and str() is
 used to compute the “informal” string representation of an object
 (a representation that is useful for printing the object).

**The print statement and str() built-in function uses __str__ to display the
string representation of the object while the repr() built-in function uses
__repr__ to display the object.
'''

import datetime

today = datetime.datetime.now()

# Prints readable format for date-time object
print(str(today))

# prints the official format of date-time object
print(repr(today))

'''Output:
2016 - 02 - 22 19: 32:04.078030
datetime.datetime(2016, 2, 22, 19, 32, 4, 78030)
str() displays today’s date in a way that the user can understand the date and time.

repr() prints “official” representation of a date - time object(means using the “official” 
string representation we can reconstruct the object).
'''

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

    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employees('{self.name}', {self.salary}, '{self.role}')"

    def __str__(self):
        return f"The name is : {self.name}, salary is :{self.salary} and the role is {self.role}"


emp1 = Employees("Ranjan", 123, "Coder")

print(emp1)
"""When we try to print the emp1 object then the operator loadibg comes into action
and the repr/str operator is returned.
calling a employees object in print function returns either repr of str function defined
.
if both functions are defined in a class then the str method is preferred while 
a class oject is printed
"""

print(repr(emp1))
"""repr method can be called by calling the method my name repr IF SRT METHOD IS ABSENT 
IN ANY CLASS"""
