# what is incapsulation?

class car:
    def __init__(self, color, brand, price):
        self.color = color
        self.brand = brand
        self.__price = price
    def start(self):
        print("car is starting")
    def get_price(self):
        return self.__price
    
c1 = car("red", "bmw", 100000)
print(c1.color)
c1.start()
print(c1.get_price())


# constractor



# inheritance



# superclass/baseclass/parentclass

# subclass/derivedclass/childclass


class person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def display(self):
        return self.name,self.age,self.gender
class student(person):
    def __init__(self, name, age, gender,roll_no):
        super().__init__(name, age, gender)
        self.roll_no = roll_no
    def display(self):
        print(super().display())
        print(self.roll_no)
        
s1 = student("kane",15,"male",2)
s1.display()

# abstraction

from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        print("Meow !!!")

a1 = Cat()
a1.make_sound()


# polymorphism
# overading




# inheritance

# encapsulation

# task
#  