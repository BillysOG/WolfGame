class Animal:
    def __init__(self,species,legs):
        self.species = species
        self.legs = legs
        
    def is_animal(self):
        print(f"{self.species} is an animal")
class Carnivore:
    def meat(self):
        print(f"{self.name} is eating meat!")

class Herbivore:
    def plant(self):
        print(f"{self.name} is eating plants!")

class Cat(Animal,Carnivore):
    species = "cat"
    num_of_cats = 0
    
    def __init__(self,name,breed,colour,age,dead):
        self.name = name
        self.breed = breed
        self.colour = colour
        self.age = age
        self.dead = dead
        Cat.num_of_cats += 1

    def sleeping(self):
        print(f"The {self.colour} {self.breed} is sleeping!")

    def playing(self):
        print(f"The {self.colour} {self.breed} is playing around!")

    def describe(self):
        print(f"{self.colour} {self.breed} that is {self.age} years old, it is a {Cat.species}!")

cat1 = Cat("Molly","Shorthair","orange",8,False)
cat2 = Cat("Blacky","Bombay","black",10,False)
cat3 = Cat("Agon","Persian","white and black",14,True)

print()

cat1.meat()
cat1.is_animal()
cat1.describe()
cat1.playing()
cat1.sleeping()
print(f"There are {Cat.num_of_cats} cats")

print()