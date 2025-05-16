#Inheritance
#Polymorphism,Abstraction,Encapsulation
""""
#Inheritance -> It allows a class called child/subclass to inherit
attributes and methods from another class called the parent/superclass
"""
#basic syntax
class Parent: #parent class
    pass

class Child(Parent):#child class that gets all the attributes and methods from the parent
    pass
#child automatically inherits everything from parent

#
class Person:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        return f"My name is {self.name}"
    def walk(self):
        return "This person is walking"

person1=Person("Haji")
print(person1.introduce()) #My name is Haji
print(person1.walk())

class Student(Person):
    def __init__(self, name):
        super().__init__(name)#this allows us to access parent methods
        #in this case,we want the student name to be used
        #as the Person name
        self.name=name

student1=Student("Robert")
print(student1.introduce()) 
print(student1.walk())  
print("<Student>",student1.introduce())

#
class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        return f"{self.name} is eating"
    
crabs=Animal("Crabs") 
print("<Animal>",crabs.eat())  

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        #self.name=name
    #by redifining the methods in the parent class.
    #we can be able to override them(polymorphism)
    def eat(self):
        return f"{self.name} is chewing sugar cane"


dog1=Dog("Bosco")
print("<DOG>",dog1.eat())

#
class Car:
    def __init__(self,model):
        self.model=model

    def drive(self):
        return f"Car of model {self.model} is being driven"

    def __repr__(self):
        return f"<Car Model: {self.model}>"  

car1=Car("Mercedes")
print(car1)
print("<Car>",car1.drive())      

class Toyota(Car):
    def __init__(self,model="Toyota"):
        super().__init__(model)

toyota1=Toyota()
print("<Toyota>",toyota1.drive())  

toyota2= Toyota("Carina")
print("<Toyota>",toyota2.drive())