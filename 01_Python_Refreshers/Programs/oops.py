# OOP (Object-Oriented Programming) example
# Classes help you group data and behavior together.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Create objects from the class
my_dog = Dog("Buddy", 3)
my_dog.bark()
my_dog.info()


# Inheritance example
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal makes a sound")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow")


cat = Cat("Milo")
cat.speak()
