
class Employee:
    work_day_per_month = 22

    def printer(self):
        '''
        WHile defining a method self means the instance which calls that method.
        if we call this method by ranjan_emp instance then self is ranjan_emp
        '''
        print("name = ", self.name)
        print("salary = ", self.salary)



ranjan_emp = Employee()
lamsal_emp = Employee()

ranjan_emp.name = "Ranjan"
ranjan_emp.salary = 100000
lamsal_emp.name = "Lamsal"
lamsal_emp.salary = 19999

print(ranjan_emp.printer())
"""WHen the method is called for ranjan then it gives the values os of ranjan_emp
becausee self is ranjan_emp in this case"""
print(lamsal_emp.printer())
"""lamsal_emp is self in this case"""


####-----  constructor
class Const:
    def __init__(self, aname, asalary, arole):
        """This is a constructor. It is used to construct objects of class
        here self means the object that is constructed uing this constructor
        aname, asalary, arole are the arguments taken"""

        self.name = aname
        self.salary = asalary
        self.role = arole

        """ name, salary and role are the instance variable of the object self
        and it maps to sname, asalary and arole arguments respectively"""

ranjan = Const("Ranjan", "100000", "Backend dev")

print(ranjan.__dict__)




