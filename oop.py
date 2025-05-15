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

    def price(self):
        print(f"The {self.brand} {self.model} is one of the few cars inspired by Formula 1 engineering.")    

    def features(self):
        print(f"It features a {self.engine} mated to a {self.transmission} gearbox.") 

    #getter method
    #@property
    #def brand(self):
     #   return self._brand.upper()

car1= Car("Mercedes","AMG ONE","hybrid 1.6L V6 engine","7-speed automated manual")
print(car1.brand)
print(car1.model)
car1.price()
car1.features()

car2=Car("Aston Martin","Valkyrie","hybrid 6.5L V12 engine","7-speed automated manual")
car2.price()
car2.features()





#using property()
"""
Properties in Python are attributes that are controlled by methods.
Python provides us a few built-in functions to manipulate attributes:
-getattr() retrieves the value of an attribute.
-setattr() changes the value of an attribute, just as you would with dot notation.
-hasattr() checks for the presence of an attribute.
-delattr() removes an attribute from a class or object.
"""
class Human:
    species="Homo sapiens"
    def __init__(self,age):
        self.age=age

    def get_age(self):  
        print("Retrieving age.")
        return self._age
    
    def set_age(self,age):
     if (type(age) in (int,float)) and (0 <= age <=120):
        print(f"Setting age to {age}")
        self._age=age
     else:
        print("Age must be a number between 0 and 120")
        
    age=property(get_age,set_age)


#class methods
#@classmethod
#def species(cls):
    #print(f"species is {cls.species}")

"""
get_age() is compiled by the property function and prints "Retrieving age" when we access age through dot notation or an attr() function.
set_age() is compiled by the property() function and prints "Setting age to { age }" when we change our human's age.
The property() function compiles our getter and setter and calls them whenever anyone accesses our human's age.
Notice the single underscore we place before the age attribute. This tells other Python programmers that this is meant to be treated as a private member of the class
"""

class Bus:
    def __init__(self,name,year):
        self._name=name
        self.year=year

    #getter method
    @property
    def name(self):
        print("internal",self._name)
        return self._name.upper()
    @property
    def year(self):
        return self._year
    #setter method
    @name.setter
    def name(self,value):
        #check value is equal to man
        if value =="man":
            self._name=value
        else:
            #the raise keyword behaves like the return keyword
            # where they both stop esxecution
            raise ValueError("Bus name must be man")
    @year.setter
    def year(self,value):
        if not isinstance(value,int):
            raise ValueError("Year must be an integer") 
        self._year=value   

bus1=Bus("man",2020)
print(bus1.name)    
bus1.year=2018
print(bus1.year)     

#scenario(example where oop can be used)
class Voter:
    def __init__(self,name,age):
        self._name=name
        self._age=age

    #getter method
    @property
    def age(self):
        return self._age

    #setter method
    @age.setter
    def age(self,value):
        if not isinstance(value,int):
            raise ValueError("Age must be an integer")
        if value >= 18:
            self._age=value
        else:
            raise ValueError("Age must be over or 18") 

    """
    ASSINGMENT:
    create a validation method for age that checks for datatype
    and also if its above or equal to 18       
    """
voter1=Voter("Jane",12)        
