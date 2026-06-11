class MyClass:
    def __init__(self, name ,age):  ##constuctor
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eatting food")


        
class Student(MyClass):

    def brak(self):
        print(f"{self.name} is taking a break")
    