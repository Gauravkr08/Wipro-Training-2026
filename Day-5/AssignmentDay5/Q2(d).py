# Demonstrate polymorphism using the same method name with different behaviors
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


animals = [Animal(), Dog(), Cat()]

for animal in animals:
    animal.sound()