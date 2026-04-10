# what is data stracture
# ans -> data stracture is a way of organizing and storing data in a way the computer can easily access and manipulate.

# types of data stracture
# 1. list
# 2. tuple
# 3. dictionary
# 4. set


# list -> list is order collection of items and mutable/changeable []
# tuple -> tuple is order collection os items and immutable/unchangeable ()
# dictionary -> dictionary is unordered collection of key value pairs and mutable/changeable {}
# set -> set is unordered collection of items and unique and mutable/changeable {}


# Example of list

colors =["red", "green", "blue", "yellow"]
print(colors)

# Now The Topic Comes Indexing
# what is indexing?
# indexing is a way to access an item in a collection by its position or index. 
# indexing is started from 0 always
# inexing is starting from 0 to n-1

# why we use indexing in python?
# Because python is a zero based language. 
# so we can access the first item in the list by indexing it as 0 or indexing the second item in the list by indexing it as 1 and so on.

# Example of indexing 

colors =["red", "green", "blue", "yellow"]
print(colors[3]) # here you enter the index number that you want to print at place of 0
# you must be remember that enter the valid index number or else you will get error message.



# mutable -> changeable
# there are two way to adding new element in list
# 1. append(value)
# 2. insert(index, value)

#example of append

colors = ["red", "green", "blue", "yellow"]
colors.append("black")
print(colors)

#example of insert

colors = ["red", "green", "blue", "yellow"]
colors.insert(2, "red")
print(colors)


# Now the topic Comes remove elements 
# there are two way to remove elements in list
# 1. pop(enter index number)
# 2. remove(enter value that you want to remove)

# Eample of the function called pop()

colors = ["red", "green", "blue", "yellow"]
removed_item = colors.pop(2)
print(colors)
print(F"removed item is {removed_item}")

# Example of the function called remove()

colors = ["red", "green", "blue", "yellow"]
removed_item = colors.remove("green")
print(colors)



# project -> create a one list that praform indexing, append, insert, pop, remove

colors =["red", "green", "blue", "yellow"]
print(colors[3]) # here code display the fourth element in the list 
colors.append("black")
print(colors) # here code display the list with new element
colors.insert(2, "red")
print(colors) # here code display the list with new element
removed_item = colors.pop(2)
print(colors)
print(F"removed item is {removed_item}")
removed_item = colors.remove("green")
print(colors)




# Now the Topic comes sort, len, remove
# sort -> sort the list
# len -> len show that length of the list
# remove -> it can remove the element from the list


# Now the Example of the Above Topic

# make a list
colors =["red", "green", "blue", "yellow", "black"]

# used remove function to remove the element from the list
colors.remove("red")
print(colors)
print(F"colors that remove :{colors}")

# sort the list
colors.sort()
print(colors)

# if you want to sort the list in reverse order then 
colors.sort(reverse=True)
print(colors)




# now we used len function 
print(len(colors))




# slicing
# slicing means getting a part of the list
# stracture of slicing is 
# list_name[start:end:step]
# example

colors = ["red", "green", "blue", "yellow", "black"]
print(colors[1:4])

# example 2

colors = ["red", "green", "blue", "yellow", "black"]
print(colors[:3])
print(colors[2:])

# example 3

colors = ["red", "green", "blue", "yellow", "black"]
print(colors[::2])




# Explain all the above topic point way why where and when we use these kind or codes
# Now we are going to explain all the topic of above in short way:
# 1. list -> list is order collection of items and mutable/changeable []
# 2. tuple -> tuple is order collection of items and immutable/unchangeable ()
# 3. set -> set is unorder collection of items and mutable/changeable {}
# 4. dictionary -> dictionary is unordered collection of the key-value pairs and mutable/changeable
# 5. indexing -> indexing is starting from 0 always
# 6. mutable -> changeable
# 7. immutable -> unchangeable
# 8. slicing -> getting a part of the list 
# 9. len -> len show that length of the list 
# 10. sort -> sort the list
# 11. remove -> it can remove the element from the list
# 12. append -> add new element in the list 
# 13. insert -> insert new element in the list
# 14. pop -> remove the element from the list