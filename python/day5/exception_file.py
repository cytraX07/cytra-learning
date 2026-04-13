#a = int(input("Enter first number: "))
#b = int(input("Enter second number: "))


#try:
#    div = a/b
#    mult = a * b
#except:
#    print("we cannot divide by zero")
#else:
#    print(f"Division: {div}")
#    print(f"Multiplication: {mult}")
#


#try:
#    c = int(input("Enter third number: "))
#    d = int(input("Enter fourth number: "))

#    div = c/ d
#    mult = c * d
      
#except ZeroDivisionError:
#    print("we cannot divide by zero")
#except ValueError:
#    print("we cannot multiply strings")
#else:
#    print(f"Division: {div}")
#    print(f"Multiplication: {mult}")

#finally:
#    print("Thank You end of the program")

# WHY WE PUT THE INPUT IN TRY BLOCK?

# create a list try to access the index which is not present in your list and handle that error

colors =["red", "green", "blue", "white", "black"]  # ye list me 5 colors hai toh try block me bhi 5 colors ke index access karenge
# or main es list ko try block main esliye nahi diya hu kyuki try block main shirf usko rakha jata hi jisme error aane ka chance hai 

try:
    enter_index = int(input("Enter the index:"))
    
    selected_color_index = colors[enter_index]
    print(selected_color_index)
except IndexError:
    print("The index that you entered is not present in the list")
except ValueError:
    print("please enter a valid index")



