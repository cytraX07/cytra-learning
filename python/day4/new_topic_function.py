# topic
# function -> function is a block of code that is used to perform a specific task

#def function_name(paramaters1, paramaters2,........., parametersn):
#    function body

def display():
    print("hello world")

#call or invoke
display()
display()

# parameters 

def add(a,b):
    sum1 = a + b
    print(f"addition : {sum1}")
    print("addition:", sum1)
    return sum1


add(10,20)
add(100,200)    


result1 = add(10,20)
print(result1)

result2 = add(100,200)
print(result2)

# what is argument?
# ans-> arguments are the values that are passed to the function

# what is function?
# ans-> function is a block of code that is used to perform a specific task

# what is the use of "f" in python?
# ans-> "f" is used to format the string


# questions -> create a function which will take a numbers which should be return the number is even or odd if the number is odd it say false and if the number is even it say true

def check_even_odd(number):
    if number%2 == 0:
        return True
    else:
        return False
    
result = check_even_odd(1)
print(result)

# global variables

count = 1

def update():
    global count
    count = 2
    print(count)

update()
print(count)

#legb


# function -> A function is a block of code that is used to perform a specific task. It can take input parameters and return output.
# 
# what is the use of "def"?
# Ans -> def is used to define a function in python.
# 
# when we use "def" in python? explain.
# Ans -> def is used for that time when we want to create a function and when we want to call a function.
#
# what do you mean by "global"?
# Ans -> global is a keyword in python which is used to declare a variable as global variable which means that the variable can be accessed from anywhere in the program.
#
# what do you mean by "local"?
# Ans -> local is a keyword in python which is used to declare a variable as local variable which means that the variable can be accessed only from within the function.
#
# what do you mean by return?
# Ans -> return is a keyword in python which is used to return a value from a function.
#
# what do you mean by "display"?]
# Ans -> display is a function in python which is used to print a message on the screen like print("hello world").
#
# what do you mean by "call"?
# Ans -> call is a keyword in python which is used to call a function.
#
# what do you mean by "invoke"?
# Ans -> invoke is a keyword in python which is used to call a function.
#
# what do you mean by "parameter"?
# Ans -> parameter is a keyword in python which is used to pass a value to a function.


# Notes
# Describe all the above code in 500 word with explanation?
# Ans -> This Python script is an educational tutorial on functions, demonstrating definition, parameters, arguments, return values, and global variables.

# 1. Introduction & Basic Function (Lines 1-12): 
# Comments define a function as "a block of code for a specific task." Syntax shown: def function_name(parameters):. display() prints "hello world" twice when called (display()). Illustrates definition (def) vs. invocation (calling).

# 2. Function with Parameters & Return (Lines 14-25):
# add(a, b):

# Takes parameters a, b.
# Computes sum1 = a + b.
# Uses f-string (f"...") for formatted print.
# Returns sum1.
# Calls: add(10,20) prints "addition : 30" twice, returns 30 (stored in result1). Same for add(100,200). Arguments (10,20) passed to parameters.

# 3. Key Concepts (Comments):

# Arguments: Values passed during call.
# f-string: Formats strings (e.g., embeds sum1).
# 4. Even/Odd Checker (Lines 40-47):
# check_even_odd(number): Returns True (even, %2==0) or False (odd). check_even_odd(1) → False, printed.

# 5. Global Variables (Lines 49-57):
# count = 1 (global). update() uses global count to modify it to 2, prints 2. Post-call, print(count) shows 2. Demonstrates scope (LEGB: Local, Enclosing, Global, Built-in).

# 6. Q&A Section (End):
#Reinforces:

# def: Defines functions.
# global: Accesses outer variables inside functions.
# return: Exits with value.
# Examples like display().
# Execution Flow:

# Runs without errors post-fix.
# Output: Two "hello world", multiple "addition : 30/300", 30/300 prints, False, two 2's.
# Learning Value:
# Teaches reusable code blocks, avoiding repetition. Functions promote modularity. Parameters/arguments enable flexibility. return allows reuse. global handles shared state (use sparingly; prefer parameters).

# Minor Notes:

# Typos: "paramaters!" (should be "parameters").
# Explanations simplify: "call/invoke" aren't keywords (just actions); no local keyword (locals implicit).
# Perfect for beginners: Hands-on, progressive complexity.
#