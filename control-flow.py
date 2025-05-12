"""CONTROL FLOW
-> The order of execution
->We are able to control the said order
"""

#conditional statemens
age=17
if age>18:
    print("you're an adult")
else:
    print("you're a kid")    #output: you're a kid


score=67
if  score>=90:
    print("grade A")
elif score >= 80:
    print("grade B")
elif score >= 50:
    print("grade C")
else:
    print("grade D")       

def grader(score):
    #checks for falsy
    if score<0 or score>100:
        return "has to be between 100 and o"


    #checks for truthy
    if score >=0 and score <=100:
        pass
    else:
        return "has to be between 100 and 0"
    
#loops using for loop
colors=['red','green','blue']

for color in colors:
    print(color) #red green blue


#range -> in built function that generates a sequence of numbers
for i in range (5):
    print(i)    #01234

count = 0
while count < 5:
    print(count)
    count +=1
print("below the while loop")    