from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animals is sleeping")


class Dog(Animal):
    def sound(self):
        print("woof woof")


class Cat(Animal):
    def sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

# animal sound
dog.sound()
cat.sound()

# animal sleeping
dog.sleep()
cat.sleep()
