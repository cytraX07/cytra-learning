# variables 
# data types
# operators
# input

# what do mean by variables?
# variables are containers for storing data values.
# variables example:
#           age = 25
#           name = "jhon"


# what are data types?
# data types are the types of values that can be stored in variables.
# data types examples:
# int
# float
# str
# bool


# what are operators?
# operators are symbols that are used to perform operations on values.
# operators examples:
# + -> addition
# - -> subtraction
# * -> multiplication
# / -> division
# % -> modulus
# ** -> exponent/power

# what is input?
# input is a function that allows you to get input from the user.
# input examples:
# name = input("Enter Your Name")
# age = input("Enter Your Age")


# variables_name = value

a = 15

# variable name rules
# your variable name must start with a letter a-z or A-Z or an underscore _
# not allowed -> 1num =5

num1 = 5

# special characters are not allowed @,#, $, %, etc and space are not allowed

first_name = "John"


age = 15


#keywords are not allowed 

# break = 10


# basic data types in python
# 1. int
# 2. float
# 3. str
# 4. boolean

# integer -> whole numbers without a decimal point

age = 25
print(type(age))

# float -> numbers with a decimal point

rating = 4.5
print(type(rating))

# string -> sequence of characters enclosed in single quotes '' or double quotes ""

#characters -> 'a', 'b', 'c', etc
#strings -> "hello", "world", "python", etc

name = 'Alice'
print(type(name))

# boolean -> represents one of two values: True or False

d = True
print(type(d))



num1 = '8'
num2 = '10'

print(num1 + num2) # concatenation

# typecasting -> converting one data type to another data type
print(int(num1) + int(num2)) # addition
print(float(num1) + float(num2)) # addition
print(str(num1) + str(num2)) # concatenation
print(bool(num1)) # True
print(bool(num2)) # True

name = "John"
print(num1) # num1 is a variable
print(name) # name is a variable and a string literal
print("Welcome") # Welcome is a string literal

name = input("Enter your name: ")
print("Welcome", name , "Have a Good Day!")
print(f"Welcome {name} Have a Good Day!")

print (f"Addition: {num1} + {num2}") # this will not work because num1 and num2 are strings
print(f"Addition: {int(num1) + int(num2)}") # this will work because we are converting num1 and num2 to integers before adding them


# why we used a word that is "type" in the above code?
# because we are using the type() function to get the information about of that variable is a string or a number or a boolean or something else

# why we used a word that is "print" in the above code?
# beacuse we are using the print() function to print the value of that variable is a string or a number or a boolean or something else

# why we used a word that is "input" in the above code?
# beacuse we are using the input() function to take data from the user.

# why we use a word that is "str" in the above code?
# beacuse we are using the str() function to convert the value of that variable in a string.

# why we use a word that is "int" in the above code?
# beacuse we are using the int() function to convert the value of that variable in a integer.

# why we use a word that is "float" in the above code?
# beacuse we use the float() function to convert the value of that variable in a float.

# why we use a word that is "bool" in the above code?
# beacuse we use the bool() function to convert the value of that variable in a boolean.

# what is concatenation?
# concatenation is the process of joining two or more strings together to form a single string.

# what is type casting?
# type casting is the process of converting one data type to another data type.

# what is string literal?
# string literal is a sequence of characters enclosed in single quotes '' or double quotes ""

# what is the meaning of sign "f" in the above code?
# f means formatted string literals or f-strings
# it allows us to embed expressions inside string literals
# using curly braces {}. The expressions are evaluated at runtime and then formatted using the format() protocol.


# project first -> create a simple calculator that takes two numbers and
#                   a mathemetican operator as input and performs the corresponding 
#                   operation (addition, subtraction, multiplication, division)
#                    and prints the result. give the name of this project as calculator.py