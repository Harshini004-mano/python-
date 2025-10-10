#overriding parent method 
class Dog(Animal): 
    def speak(self): 
        print("Dog barks") 
 
d = Dog() 
d.speak()  # Dog barks 