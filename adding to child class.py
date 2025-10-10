#adding to child class 
class Dog(Animal): 
    def bark(self): 
        print("Woof!") 
 
d = Dog() 
d.bark()      # Woof! 
d.speak()     # Animal speaks 