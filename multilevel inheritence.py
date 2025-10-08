class grandparent:
    def speak(self):
        print("animal speak")
class parent(grandparent):
    pass
class child(parent):
    pass

a = child()
a.speak()