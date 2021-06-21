"""Donot Repeat Yourself"""

'''
Classes are just like template... we can create a class...give it
a bunch of attributes and ehenever we need those attributes we 
define a object of that class(Type).
So code reusability, and efficiency is experienced
'''
"""
Class − A user-defined prototype for an object that defines
 a set of attributes that characterize any object of the 
 class. The attributes are data members (class variables 
 and instance variables) and methods, accessed via dot notation.
"""
class Student:
    pass

ranjan = Student()
lamsal = Student()
''' 
We can create an object of that class just by defining the 
objects by calling the class
Here ranjan and lamsal are two different Student(class) objects
that are stored in diff memory locations

Object − A unique instance of a data structure that's defined 
by its class. An object comprises both data members 
(class variables and instance variables) and methods.
'''
# print(ranjan, lamsal)


"""
Instance − An individual object of a certain class. 
An object obj that belongs to a class Circle, for example, 
is an instance of the class Circle.
"""



ranjan.name = "Ranjan"
ranjan.std_year = 1
ranjan.group = "CE"
ranjan.subjects = ['maths', 'Basic Engg', 'EDRG', 'Physics']
"""
Now we can also create instance variables of objects
Instance variable − A variable that is defined inside a 
method and belongs only to the current instance of a class. 
"""
"""
We can pass strings, numbers , lists tuple, dict or any data types in 
instance variable
"""
print(ranjan.group)
print(ranjan.name)
'''
We can access the instances variables by writing the object name
to which it belongs along with a dot and then variable name
'''


###----  CLass variable ---####

'''
Class variable − A variable that is shared by all instances
 of a class. Class variables are defined within a class
  but outside any of the class's methods. Class variables 
  are not used as frequently as instance variables are.
  class variable must be defined inside the class
  
'''

class Employee:
    work_day_per_month = 22
    """
    This is a class variable and its scope is anywhere inside
    this class. object defined under this class also can access the 
    class variable
    """
    pass

ranjan_emp = Employee()
lamsal_emp = Employee()

ranjan_emp.name = "Ranjan"
ranjan_emp.salary = 100000
lamsal_emp.name = "Lamsal"
lamsal_emp.salary = 19999

"""
These are instance variables and are created and can be accessed
under that object. These variables are the properties of that
particular object. 
"""

print(ranjan_emp.work_day_per_month) #accessd by instance ranjan
print(lamsal_emp.work_day_per_month) #accessd by instance lamsal
print(Employee.work_day_per_month) #accessd by class

Employee.work_day_per_month = 20
'''changing work_day_per_month from 22 to 20
Can be changed from the class '''
print(ranjan_emp.work_day_per_month) #20
print(Employee.work_day_per_month) #20


"""
Now if we try to change the class variable from any of the instances
(ranjan_emp or lamsal_emp) then instead of changing the class variable
a new instance variable is created and the value is assigned
to that instance variable
"""

ranjan_emp.work_day_per_month = 25
"""Here the class variable work_day_per_month is not changed
instead a new instance variable for ranjan is created"""
print(Employee.work_day_per_month) #20
print(ranjan_emp.work_day_per_month) #25
print(lamsal_emp.work_day_per_month) #20


#-----   __dict__ attribute  ---####
print(ranjan_emp.__dict__)
print(Employee.__dict__)

"""
instance.__dict__ does nothing but returns all the instance variables, attributes 
and methods of instance or class and their values as keys and values in dict form
"""