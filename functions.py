""" FUNCTIONS
1. Blocks of reusable code
2. Created using the def keyword

"""
#function defination
def hello(name):
    print(f"Hello {name},we are learning about functions")

#calling the function
hello("Daud")

#1.Positional arguements
def greeting (first_name, last_name):
    print(f"Goodmorning, {first_name} {last_name}")
greeting("Daud", "Ahmed") #order matters when passing arguements

#Keyword arguements where are identified by the parameter name which basically make the order irrelevant
greeting(last_name="Kimani",first_name="Vincent") #Vincent Kimani

#an unknown number of positional args
#the unknown values will automatically be passed to a tuple
def sum(*args):
    #sum is an inbuilt function -> a bit similar to the reduce method in js
    print(args)
sum(1,2)    #(1,2)

#Decorators -> reusability
"""
-> Design patterns that allows us to modify the functionality of a function without necessarily 
modifying the function code itself
-> It uses the special @ symbol on functions
"""
#how to create decorators
def logger(func):
    #define another inner function
    def inner():
        print("Decorator is running before function")
        #execute the original function
        func()
    return inner

@logger
def check_mic():
    print("Is the mic working?")

check_mic()    

decorated_func = logger(check_mic)
#call/execute the inner function
decorated_func()

def modifier(func):
    def inner(a,b):
        #modify argument a
        a=a+5
        print(a)
        #call the original function
        return func(a,b)

    return inner
@modifier
def calculate(a,b):
    return a + b

print (calculate(3,3))