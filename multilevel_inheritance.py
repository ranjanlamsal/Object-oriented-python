#opps9

class Grandfather:
    basketball = 1
    football = 1
    cricket = 1

class Father(Grandfather):
    language = 4
    football = 2
    cricket = 2

    def print_lang(self):
        return f"I speak {self.language} no of languages"

class Son(Father):
    language = 6
    cricket = 3
    def print_lang(self):
        return f"Yes i speak {self.language} no of languages"

huma = Grandfather()
daya = Father()
ranjan = Son()

print(ranjan.print_lang())
print(ranjan.basketball)
"""At multilevel inheritance, if a class class 2 is inherited from class1 . and when 
class 2 is inherited to class3 then all the attributes, variables, methods of class
2 can be assecced by class3. In addition to this all the attributes, methods and variables
of class1 is also inherited """

print(ranjan.football)
"""From class Father(). Grandfather class also contain the same variable 
but if the variable is present in the nearest ancestor class, it will be returned
"""
print(ranjan.cricket)
"""From self class"""