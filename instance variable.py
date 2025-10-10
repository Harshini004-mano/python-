#instance variable

class Dog: 
      def __init__(self, name): 
          self.name = name  # instance variable 
d1 = Dog("Max") 
d2 = Dog("Buddy") 
print(d1.name)  # Max 
print(d2.name)  # Buddy 