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
