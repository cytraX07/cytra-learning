num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))

# int -> addition, subtraction, multiplication, division, floor division, remainder, power 

print(f"Addition : {num1 + num2}") # f means formatted string literals or f-strings, 
                                # it allows us to embed expressions inside string literals, 
                                # # using curly braces {}. The expressions are evaluated at 
                                # # runtime and then formatted using the format() protocol.

print(f"Subtraction : {num1 - num2}")
print(f"Multiplication : {num1 * num2}")
print(f"Division : {num1 / num2}")
print(f"floor Division : {num1 // num2}") # floor division -> it returns the largest integer less than or equal to the result of the division 
print(F"Remainder : {num1 % num2} " ) # remainder -> it returns the remainder of the division of num1 by num2 
print(f"power : {num1 ** num2}") # ** ->  power operator -> it returns the result of num1 raised to the power of num2 
