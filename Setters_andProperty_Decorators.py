class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@newmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}."

    def email(self):
        return f"{self.fname}.{self.lname}@newmain.com"

    @property
    def printemail(self):
        return f"{self.fname}.{self.lname}@newmain.com"


ranjan = Employee("Ranjan", "Lamsal")

print(ranjan.explain())
print((ranjan.email()))

"""Now if we want to change any instance of the class. In this case lets change 
Ranjan to RANJAN"""

ranjan.fname = "RANJAN"

print(ranjan.explain())
"""Here fname is changed because the parameter f.name is specified while creating 
the object but then it is changed to different value. After that only te printemail 
functiom is called which use the f.name value. And hence the changed name is printed"""
print((ranjan.email()))
"""In this case the value is not changed because the variable email is the
instance of the class and thus is created while the creation of the object.
And email instance got the initial value of the instances while creating the object

We can do is define a function that return the value we want by calling the instances
in te function. So if the function is called after changing the value , function had the
new value of the instances and return the new result
"""

#### Property decoretor ####
"""@property decorator is a built-in decorator in Python which is helpful 
in defining the properties effortlessly without manually calling the inbuilt
 function property(). Which is used to return the property attributes of a 
 class from the stated getter, setter and deleter as parameters."""

print(ranjan.printemail)
"""Here the setter decorator changed the function into attribute """

### Setters ###
"""Among above example if we change the email and accordingly the fname and lname
are also changed then we use setters
Actually the attributes cannot be changed or set in python unlsee we use setter decorator
"""
class Employee2:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@newmail.com"


    def explain(self):
        return f"This employee is {self.fname} {self.lname}."


    def email(self):
        return f"{self.fname}.{self.lname}@newmain.com"


    @property
    def printemail(self):
        if self.fname == None or self.lname == None:
            return "Email is not set"
        else:
            return f"{self.fname}.{self.lname}@newmain.com"

    @printemail.setter
    def printemail(self, string):

        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @printemail.deleter
    def printemail(self):
        self.fname = None
        self.lname = None
"""The deleter decoretor is used to delete any attribute .. By the way modify the 
attrubute. SO for deleting we set the attribut to None"""




ranjan2 = Employee2("Ranjan","Lamsal")
# ranjan2.printemail = "This.That@newmail.com"

print(ranjan2.fname)
print(ranjan2.lname)
"""Now the fname and lname are changed to this and that as we changed the mail
and then set the mail. And redefined the fname and lmane in the printemail attribute"""


del ranjan2.printemail
"""When del is called then the program search for the deleter and change the 
instance as defined in deleter"""
print(ranjan2.printemail)