#class variable
class Dog: 
    species = "Canine"  # class variable 
 
    def _init_(self, name): 
        self.name = name 
 
print(Dog.species)  # Canine 