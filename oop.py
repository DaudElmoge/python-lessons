# Remember that Python requires some indented code in each code block.
# Instead of empty blocks, we use the "pass" keyword to do nothing.

class Dog:
    pass

fido = Dog()
fido

snoopy=Dog()
snoopy

lassie=Dog()
lassie

fido.__dir__()

"""
Principles of OOP
1.Inheritance
2.Abstraction
3.Encapsulation
4.Polymorphism

-> Involves the use of classes and objects
-> It has methods and properties (attributes)
"""

#class -> its a blueprint of how objects are created and how they behave.
#Below is an example of a student entity
#Attributes -> name,class,grade,gender
#Behaviors -> read,playing a game,partying,rebellious 

#Example in Food
#Attributes ->ingredients,hot/cold,origin,calories,prep time
#Behaviours ->

#Scenario -> A client wants a system that tracks their fleet of cars/mats 
#plus passengers,daily trips and all that

'''
Entity Car -> color,number plate,brand,capacity,driven,stop
Entity Driver -> name,age,dl
Entity Trip -> 
'''

#syntax
class Student:
    #"_init_"should always be present when creating classes in python
    #it always takes self as its first parameter
    #this method is always automatically called when a new instance is created

    def __init__(self,name,age):
        #instance attributes
        self.name=name
        self.age=age
#We use methods to define bahviours
#it always takes self as the first parameter
    def read(self):
        print(f"{self.name} is reading about oop")

    def play(self):
        print(f"{self.name} ")    

#creating an instance at the student class    
Student1=Student("Trevor",20)
print((Student1.name))#Trevor
print(Student1.age)#20
Student1.read()

student2=Student("Edna",23)
print(student2.name)#Edna
print(student2.age)#age
student2.read()

student3={
    "name":"Brian",
    "age":25
}

#assignment(Tue-13/5/25)-> create a class with 3-4 attributes and 2 methods (behaviors)

class Car:
    def __init__(self,brand,model,engine,transmission):
        self.brand=brand
        self.model=model
        self.engine=engine
        self.transmission=transmission

    def expensive(self):
        print(f"The {self.brand} {self.model} is one of the few cars inspired by Formula 1 engineering.")    

    def features(self):
        print(f"It features a {self.engine} mated to a {self.transmission} gearbox.") 

car1= Car("Mercedes","AMG ONE","hybrid 1.6L V6 engine","7-speed automated manual")
print(car1.brand)
print(car1.model)
car1.expensive()
car1.features()

car2=Car("Aston Martin","Valkyrie","hybrid 6.5L V12 engine","7-speed automated manual")
car2.expensive()
car2.features()


