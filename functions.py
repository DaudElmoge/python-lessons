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

