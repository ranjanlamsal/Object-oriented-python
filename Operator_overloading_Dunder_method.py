"""

Operator Overloading means giving extended meaning beyond their predefined
operational meaning. For example operator + is used to add two integers as
well as join two strings and merge two lists. It is achievable because ‘+’
operator is overloaded by int class and str class. You might have noticed that
 the same built-in operator or function shows different behavior for objects
 of different classes, this is called Operator Overloading.

 Binary Operators:
Operator	Magic Method
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)
Comparison Operators :
Operator	Magic Method
<	__LT__(SELF, OTHER)
>	__GT__(SELF, OTHER)
<=	__LE__(SELF, OTHER)
>=	__GE__(SELF, OTHER)
==	__EQ__(SELF, OTHER)
!=	__NE__(SELF, OTHER)
Assignment Operators :
Operator	Magic Method
-=	__ISUB__(SELF, OTHER)
+=	__IADD__(SELF, OTHER)
*=	__IMUL__(SELF, OTHER)
/=	__IDIV__(SELF, OTHER)
//=	__IFLOORDIV__(SELF, OTHER)
%=	__IMOD__(SELF, OTHER)
**=	__IPOW__(SELF, OTHER)
>>=	__IRSHIFT__(SELF, OTHER)
<<=	__ILSHIFT__(SELF, OTHER)
&=	__IAND__(SELF, OTHER)
|=	__IOR__(SELF, OTHER)
^=	__IXOR__(SELF, OTHER)
Unary Operators :
Operator	Magic Method
–	__NEG__(SELF, OTHER)
+	__POS__(SELF, OTHER)
~	__INVERT__(SELF, OTHER)
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

    def __add__(self, other):
        return self.salary+other.salary

    def __truediv__(self, other):
        return self.salary/other.salary

emp1 = Employees("Ranjan", 2211, "Coder")
emp2 = Employees("lamsal", 1111, "Tutor")

print(emp1+emp2)
"""Here addition operator is overloaded and the salary of the objects created are
added """

print(emp1/emp2)