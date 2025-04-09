class Animal:
    def __init__(self, name):
        self.name = name
        
    def move(self):
        pass  # To be overridden by subclasses
        
    def introduce(self):
        print(f"I am a {self.name}!")
        
class Bird(Animal):
    def move(self):
        print(f"{self.name} is flying! 🕊️")
        
class Fish(Animal):
    def move(self):
        print(f"{self.name} is swimming! 🐟")
        
class Snake(Animal):
    def move(self):
        print(f"{self.name} is slithering! 🐍")
        
class Kangaroo(Animal):
    def move(self):
        print(f"{self.name} is hopping! 🦘")  

print("\n=== Polymorphism Challenge ===")
animals = [
    Bird("Eagle"),
    Fish("Salmon"),
    Snake("Cobra"),
    Kangaroo("Joey")
]

for animal in animals:
    animal.introduce()
    animal.move()
    print()  