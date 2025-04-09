class Superhero:
    def __init__(self, name, secret_identity, powers):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers
        self.energy = 100
    
    def use_power(self):
        if self.energy >= 20:
            print(f"{self.name} uses their powers!")
            self.energy -= 20
        else:
            print(f"{self.name} is too tired to use powers!")
    
    def rest(self):
        self.energy = 100
        print(f"{self.name} rests and regains energy!")
    
    def introduce(self):
        print(f"I am {self.name}, secretly {self.secret_identity}!")
        print("My powers include:")
        for power in self.powers:
            print(f"- {power}")

# Inherited class
class Mutant(Superhero):
    def __init__(self, name, secret_identity, powers, mutation_level):
        super().__init__(name, secret_identity, powers)
        self.mutation_level = mutation_level
    
    def use_power(self):  # Overriding the method
        if self.energy >= 15:  
            print(f"{self.name} uses mutant powers with level {self.mutation_level}!")
            self.energy -= 15
        else:
            print(f"{self.name} needs to rest!")
    
    def evolve(self):  # Unique to Mutant class
        self.mutation_level += 1
        print(f"{self.name}'s mutation level increases to {self.mutation_level}!")

# Example usage
print("=== Superhero Demo ===")
spiderman = Superhero("Spider-Man", "Peter Parker", 
                     ["Web-slinging", "Spider-sense"])
spiderman.introduce()
spiderman.use_power()

print("\n=== Mutant Demo ===")
wolverine = Mutant("Wolverine", "Logan", 
                  ["Healing factor", "Adamantium claws"], 10)
wolverine.introduce()
wolverine.use_power()
wolverine.evolve()