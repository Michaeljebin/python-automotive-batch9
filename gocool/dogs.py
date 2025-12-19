# class is a keyword used to define a new class
class Dog:
    # constructor: runs every time an object is created
    def _init_(self, name, age):
        self.name = name   # e.g., "Lucy"
        self.age = age     # e.g., 4

    # behavior (method) of the Dog class
    def bark(self):
        return f"{self.name} is barking!"

# objects (instances of the class)
dog1 = Dog("Lucy", 4)
dog2 = Dog("Tommy", 3)

# calling methods
print(dog1.bark())
print(dog2.bark())