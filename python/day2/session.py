# comparison operators: ==, !=, <, >, <=, >=, is, is not 
# logical operators: and, or, not
# conditional operators -> if, elif, else, if else, nested if else
# loops 


# what is comparison oprators?
# comparison operators are used to compare two values and return a boolean value (True or False) based on the comparison. 

c = 8
b = -5

print(c > b)

# Describe the use of if, else, elif statements in Python.
# if statement is used to execute a block of code if a specified condition is true. 
# else statement is used to execute a block of code if a specified condition is false.
# elif statement is used to check multiple conditions. It stands for "else if".
# The syntax for if, else, elif statements is as follows:
# if condition:
#     # block of code to be executed if the condition is true
# elif condition:
#     # block of code to be executed if the condition is true
#     # and the previous condition was false
#   else:
#     # block of code to be executed if all the above conditions are false 
# Example: first Given Below ->
a = int(input("Enter a number: "))
if a > 0:
    print(F"{a} is positive")
elif a == 0:
    print(F"{a} is neither positve nor negative")
else:
    print(F"{a} is negative")

# Project 1 :
# Write a Python program that takes a traffic light color as input and prints the corresponding action (e.g., "Stop" for red, "Get ready" for yellow, "Go" for green).
color = (input("Enter a traffic light name: ").lower())
if color == "red":
    print("Stop")
elif color == "yellow":
    print("Get ready")
elif color == "green":
    print("Go")
else:
    print("Invalid traffic light name")

# project 2:
# Write a Python program that takes a number as input and checks if it is even or odd. 

num = int(input("Enter the Number:"))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# username -> abc 
# password -> abc1234

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "abc" and password == "abc1234":
    print("Login successful")
elif username == "abc" and password != "abc1234":
    print("Invalid password")
else:
    print("Invalid username or password")

# project 3 
# Write a Python program that takes a year as input and checks if it is a leap year or not.
# condition -> if the year is divisible by 4 and not divisible by 100 or divisible by 400

leap_years = int(input("Enter a year: "))

if (leap_years % 4 == 0 and leap_years % 100 != 0) or leap_years % 400 == 0:
    print(F"This years {leap_years} is leap_years")
else:
    print(F"This years {leap_years} is not leap_years")

# project 4
# Write a Python program that takes a student's marks as input and prints the corresponding grade based on the following criteria:
# 90-100 -> A
# 80-89 -> B
# 70-79 -> C
# 60-69 -> D
# <60 -> F

marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("grade: A")
elif marks >= 80 and marks <= 89:
    print("grade: B")
elif marks >= 70 and marks <= 79:
    print("grade: C")
elif marks >= 60 and marks <= 69:
    print("grade:D")
else:
    print("grade: F")
