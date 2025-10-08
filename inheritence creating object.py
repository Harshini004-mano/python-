class animal:
    def speak(self):
        print("animal speaks")
class dog(animal):
    pass
a=animal()
a.speak()
d=dog()
d.speak()