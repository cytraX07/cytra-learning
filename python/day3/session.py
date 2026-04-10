# loops
# for loop
# while loop

# loops -> repeat a block of code multiple times based on a condition
# for loop -> repeat a block of code for a fixed number of times
# while loop -> repeat a block of code as long as a condition is true 

# when to use for loop and when to use while loop
# use for loop when you know the number of iterations or when you want to iterate over a sequence (like a list, tuple, string, etc.)
# use while loop when you want to repeat a block of code until a certain condition is met or when you want to create an infinite loop (which can be broken with a break statement)
# for loop syntax
# for variable in sequence:
#     # block of code to be executed for each iteration
# while loop syntax
# while condition:
#     # block of code to be executed as long as the condition is true


# for loop example 1st example
# i = 0, 1, 2, 3, 4
# for i in range(start, end+1, step):
# 
for i in range(5):
    print("Hello")

for i in range(1, 6):
    print("Hello, World!")

# for loop example 2nd example

# print the numbers from 10 to 1 in reverse order
for  i in range(10, 0, -1):
    print(i)


# while loop
# why we use while loop ->
# we use while loop when we want to repeat a block of code until a ceartain code is met or when we want to create an infinite loop (which can be broken with a break statement)
# while loop syntex -> while condition:

count = 1

while count <= 10:    # count = count + 1
    print(count)        # print(count) is the block of code to be executed as long as the condition is true 
    count = count + 1  # incrementing the count variable to aviod infinite loop 



# username and password  abc abc123 3 attempts

attempts = 1

while attempts <= 3:
    username = input("Enter Your Username:")
    password = input("Enter Your Password:")

    if username == "abc" and password == "abc123":
        print("login succesfull")
        break
        
    else:
        print("Invalid username or password. Please try again.")
        attempts += 1

# while loop example 2nd example
for i in range(1,11):
    if(i == 5):
        break
    print(i)



# Exaplation of the above code:
# The code is a simple implementation of a login system that allows the user to enter their username and password. 
# The user has three attempts to enter the correct credentials. 
# if the user enters the correct username ans passoword ("abc" and "abc123"). 
# the program will print "login successful" and break out of the loop using the break statement.
# if the user enters the incorrect username or password, the program will print "Invalid username or password. Please try again." 
# and increment the attempts variable by 1.

# Explain the difference between for loop and while loop
# for loop is used to repeat a block of code for a fixed number of times,
# while loop is used to repeat a block of code as long as a condition is true.

# Why we use range function in python
# range function is used to create a sequence of numbers.

# Define all the keyword that is used in the above code
# break -> used to break out of a loop
# continue -> used to skip the current iteration of a loop
# if -> used to check if condition is true
# else -> used to check if condition is false 
# elif -> used to check multiple conditions
# for -> used to iterate over a sequence (like a list, tuple, string, etc.)
# while -> used to repeat a block of code as long as a condition is true
# in -> used to check if a value is in a sequence(like a list, tuple, string, etc.)
# range -> used to create a sequence of numbers
# print -> used to print a value
# input -> used to get input from the user


# some important project for practise of the above code from basic to advanced level is given below:
# 1. write a python program to print the numbers from 1 to 10 using for loop and name these projects file as for_loop.py
# 2. write a python program to print the numbers from 1 to 10 using while loop and name these projects file as while_loop.py
# 3. write a python program to print the numbers from 10 to 1 using for loop and name these project file as reverse_for_loop.py
# 4. write a python program to print the numbers from 10 to 1 using while loop and name these project file as reverse_while_loop.py

