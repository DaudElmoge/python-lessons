#Object relationships

#one to many
class Parent:
    def __init__(self,name):
        self.name=name
        #we will use this to store instances of the child class
        self.children = []

    def add_child (self,child):
        self.children.append(child)

class Child:
    def __init__(self,name):
        self.name=name 

    def __repr__(self):
        return f"Child {self.name}"    

parent1= Parent("Jane")
child1= Child("Tabitha")
child2= Child("Trevor")
#we can now be able to save child info to the parent class
parent1.add_child(child1) 
parent1.add_child(child2) 

print(parent1.children)#[Child Tabitha, Child Trevor]

parent2= Parent("John")
child3= Child("Ian")
parent2.add_child(child3) 

print(parent2.children)

