# create a fd list then you can a user how many value they want to add and accordingle user loop you can use append function to add value inside that


# what is object and class and attribute
# class ->
# object ->
# attribute ->

#instance variaable 
# self
# __init__
# insialise the attribute
# counstractor
# object creation
# distructor

# class Cake:
#     # condtractor
#     def __init__(self, size, flavour):
#         # instance variable
#         self.size = size
#         self.flavour = flavour
#     def display(self):
#         print(self.size)
#         print(self.flavour)

# # object creation
# c1 = Cake("small", "vanilla")
# c1.display()

# create a class called person create a cpunstractor and the attrabute of the 
# person is name and age the create the display method which display the name and age
#  of the person and create called display method


class person:
    # class variable
    shop_name = "cake shop"
    def __init__(self, name, age):
        # instance variable 
        self.name = name
        self.age = age
    def display(self):
        print(self.name)
        print(self.age)
    # distructor
    def __del__(self):
        print("object deleted")
# object creation

person1 = person("ram", "25")
person1.display()
print(person1.shop_name)

del person1



person2 = person("shyam", "30")
person2.display()
print(person2.shop_name)


# 