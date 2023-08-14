# 24 Jul 2025 being, first steps to Machine vision
'''
[-----------] Python Beginner (https://www.youtube.com/watch?v=rfscVS0vtbw) [4h]
'''
# Basics
print("\"Hellow World!\"\n")
# - Python is sequential compilation

# Variables
charAge = "35"
print("You are" + charAge + "years old!")
print(charAge)
'''
- No need to explicitly declare what variable type is presented, e.g. floats vs long vs long long vs bool (represented at True/False)
'''

# String manipulation
'''
- var_name.upper().isupper() # checks if it's all upper
- len(var_name) # checks length
'''
varPhrase = "Giraffe Academy"
print(varPhrase[3]) # Grabs a from the phrase

print(varPhrase.index("Acad")) # position of where Acad is

# Arithmetic
print(10%3)
print(abs(-10))
print(pow(2,4)) # 2^4
print(max(4,6)) # returns larger of 2, min(4,6)
print(round(3.7)) # round down or up
from math import * # allows sqrt(46) and ceil(3.7) # roundup

# IO
name = input("Enter your name")
print("Your name is " + name)
num1 = input("Enter first num")
num2 = input("Enter first num")
result = float(num1) + float(num2) # force converts num1 & num2 into float

# Lists (array in C++)
friends = ["Kevin", 2, "Karen", "Jim"]
print(friends[1:3]) # prints text from 1-3
friends.append("Creed") # Adds Creed to end friends list
friends.extend(num1) # combines both arrays
friends.pop("Creed") # removes creed
print(friends.index("Kevin")) # location of index
print (friends.count("Kevin"))
friends.sort() # ascending order
friends2 = friends.copy()

# Tupple
