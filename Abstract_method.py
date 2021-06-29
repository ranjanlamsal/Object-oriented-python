'''T
he abstract method holds all the cards because it is necessary for all classes
 that are being derived by the abstract class to have the same method even
 though their functionality and code msy differ. However, the name of method
 should be the same as the abstract method. The abstract method inside the
 abstract class could even be empty because we can not implement it anywhere.
 It is just so that all the other classes define a method by the same name.

*** Abstract methods are defined in the abstract class.
Mostly they do not have the body, but it is possible to have abstract
methods with implementation in the abstract class. Any subclass deriving from
 such abstract class still needs to provide an implementation for that abstract
  methods.

***An abstract class can have both abstract methods as well as concrete methods.
***The abstract class works as a template for other classes.

***By using the abstract class, we can define a structure without providing a
proper implementation of every method.

***It is not possible to create objects of an abstract class because
Abstract class cannot be instantiated.
***An error will occur if the abstract method has not been implemented
in the derived class.

'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())
