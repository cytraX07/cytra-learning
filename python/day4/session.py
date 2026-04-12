# list -> ordered and mutable []
# tuple -> ordered and immutable ()

# dictionary -> unordered and mutable {key:value} key -> value

# set -> unordered and mutable it only contains unique values
# popfunction -> remove last element
numbers =(1,2,3,4,5)
print(numbers[3])


numbers = numbers +(6,)
print(numbers)

students = { "A1": "jack", "A2":"jia", "A3":"joe", "A4":"jim"}

print(students)

print(students["A2"])

print(students["A5"])  # rays KeyError 
print(students.get("A5"))

# add

students["A5"] = "jane"
print(students)

# update
students["A3"] = "jane"
print(students)

# remove

deleted_item = students.pop("A6", "not found")
print(deleted_item)
print(students)



number = {5,8,9,5,7}
print(number)

#add

number.add(10)
print(number)

#remove

number.remove(5)
print(number)

# discard

number.discard(44)
print(number)

# union, intersection, difference, symmetric difference

colors1 = {"red", "blue", "green", "yellow", "orange"}
colors2 = {"blue", "yellow", "green", "black"}

print(colors1.union(colors2))

print(colors1.intersection(colors2))

print(colors1.difference(colors2))

print(colors1.difference(colors2))

print(colors2.difference(colors1))

print(colors1.symmetric_difference(colors2))


#  Question 1 create any two set it can be any things like colors, numbers, names, etc. and try all the operations like union, intersection, difference, symmetric difference


numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers2 = {5, 8, 9, 4, 11, 7, 12, 18}

print(numbers1.union(numbers2))
print(numbers1.intersection(numbers2))
print(numbers1.difference(numbers2))
print(numbers1.difference(numbers2))
print(numbers2.difference(numbers1))
print(numbers1.symmetric_difference(numbers2))


