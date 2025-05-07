"""
Rules associated with variables .
1. naming convention is snake_case
2.cannot use keywords i.e. def, class, if, else, elif, for, while, try, except, finally
3.variables must contain values when initialized
4.we use indentation to define scope/block.
5.have descriptive names.
6.functions must be defined with def keyword
7. we do not use semicolon at the end of the line

"""
#strings
message="intro to python"
print(type(message))

#interpolation in python using f-string
# f-string is a way to format strings in python
first_name="John"
full_name=f"{first_name} Doe"
print(full_name)

#integers and floats
"""
-integers are whole numbers
-floats are decimal numbers
-converting an integer to a float is done by using the float() function
-converting a float to an integer is done by using the int() function
"""
print(type(1)) #int
print(type(1.0)) #float
total=0.7+2.5
print(total) #3.2
print(type(total)) #float
print(type(7/3))# float
print(type(6/3))# float

print(round(2.5+1.4)) #4-rounded off from 3.9 to 4


#booleans
"""
booleans are logical statements that can be either True or False
"""
is_adult=True #True should be capitalized
is_child=False #False should be capitalized
print(bool(""))#False-> empty string is False
print(bool(0))#False-> 0 is False
print(bool(1))#True-> 1 is True
print(bool("False"))#True-> non-empty string is True

"""Dictionaries->they are basically objects
#dicts are collection of data stored in key-value(can be of any data type) pairs
#we still use the curly braces{}
"""

person={
    "name":"John",
    "age":4
}
print(person["age"])#4
print(person.get("age"))#4
print(person["name"])#John
print(person.get("name"))#John

person={
    "name":"John",
    "age":4,
    "address":{"county":"Mombasa"
               }
}
print(person["address"]["county"])#Mombasa
print(person.get("address").get("county"))#Mombasa

student={
    "name":"Daud",
    "age":20,
    "major":"Software Engineering",
    "scores":[34,89,76 ,{"model":"Python"}],
    "location":"Mombasa"
}
#Accesing items in a dictionary -> we can use square brackets or the get() method
print(student["name"])#Daud
print(student.get("name"))#Daud
print(student["scores"])#[34,89,76]
print(student["scores"][3].get("model"))

#Adding or updating items in a dictionary -> as long the key exists we can update the value else its going to add.
#Modifying age
student["age"]=25
student["class"]= "Web 9"
print(student)
student["class"]={
    "name":"Web 9",
    "location":"Remote"
}

print(student["class"]["location"])#Remote
print(student["scores"][2])#76

#delete items -> we use the del keyword or the .pop() method
del student["location"]
print(student)
delete_value=student.pop("class")
print(student)
print(delete_value)# {'name': 'Web 9', 'location': 'Remote'}
#the pop method returns the value of the deleted key

"""
sets -> unique elements -> we can create a set using the set() function or by using curly braces {}
"""
random_values={2,3,4,3,2,4,5}
print(random_values)#{2,3,4,5} -> duplicates are removed

#empty curly braces still fall under dictionary
# so to create an empty set we use the set() function
empty_set={}
correct_empty_set=set()#this is a set -> this is how we create an empty set
#sets avoid duplicates
print(type(correct_empty_set))#<class 'set'> -> this is a set
print(type(empty_set))#<class 'dict'> -> this is a dictionary not a set
numbers=[2,2,4,5,2]
unique_numbers=set(numbers)
print(unique_numbers)#{2,4,5} -> duplicates are removed
names=["John","Doe","John"]
unique_names=set(names)
print(unique_names)#{'Doe', 'John'} -> duplicates are removed

#lists,tuples
#tuples are immutable 
#lists are mutable

scores=(1,2,3,4,5) #example of tuple
cart=["milk","bread","eggs"] #example of list

#none -> combines null and undefined
day=None #example of none, used to indicate that a variable has no value
day="Monday" #assigned value after value is known

