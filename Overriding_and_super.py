
class A:

    classvar1 = "I am in class variable in calss A"
    classvarA = "I am solely class var in class A"
    def __init__(self):
        self.special = "This is a special variable in class A's constructor"
        self.var1 = "I am inside classA's constructor"
        self.classvar1 = "Instance var in class A"


class B(A):
    classvar2 = "I am in class B"
    classvarB = "I am only a class Variable"
    var1 = "Instance var in class A redefined in class B"

    def __init__(self):
        self.classvar2 = "Now I am a instance var in class B"
        self.classvar1 = "Instance var in class A redefined in instsncr of  class B"


a = A()
b = B()

print(b.classvar2) #from B's constructor
print(b.classvar1) #from B's constructor
print(b.var1) #from B class
print(b.classvarB) #from B class
print(b.classvarA) #from A class

"""
here we have overridden the constructor so the constructor of class B in only accessed
but that of A os not. So any instance variables or methods of constructors of class
A isnot accessed. Hence while calling var1 without defining it in calss B shows error

"""

class C(A):
    classvarA = "Class var A modified in class c"
    var1 = "Instance var of class A modified in class C"


c = C()

print(c.classvarA)
"""The classvarA of class A is overridden in class C. Since the object of class C
is made , the classvarA now returns the value as defined in class C"""
print(c.var1)
"""The var1 in overridden in class C but here when we call the var1 we dont actually 
 get it from class C first insted it returned the classA 's value. This is because
 the var1 is defined in constructor in class A i.e is the instance variable of class A
 . Hence the object while constructed takes the instance variable first.
 """

"""
Conclusion: Any variable is called then it is first looked into the self class
constructor. if no constructor present then tha parent's constructor is searched.
And then the self class is searched and finally parents class is searched (Nearest
possible parent)
"""

###Now to run the constructor of both class (Parent and offspring)

class D(A):
    classvarD = "I am D class's variable"
    classvarA = "Class A's var modified in class D"
    def __init__(self):
        super().__init__()
        self.special
        self.var1 = "A new var1 in D"

d = D()

# print(d.special)
"""ABove line shows error because the constructor of class A is overridden in class
D and hence the instances of A cannot be accessed . To accedd these we need to 
call the super().__init() constructor of class A inside the constructor of class D
"""

print(d.special)
"""We got the instance defined in class A

Now the var1 instance is defined in both class A's constructor and class D's constructor
"""

print(d.var1)
"""It returns the value as defined in constructor of class D

This is because while the constructor of class A is calles
the instances of class A are accessed. Now the value of var1 is as defined in class 
A. Now after that the var1 is redefined (Overridden ) in the cinstructor of class D
so the value is as defined in class D. Now if we do not defined the var1 in class D then 
the instances of class A (var1) is returned"""