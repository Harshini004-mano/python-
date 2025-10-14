class Parent:
    def __init__(self):
        print("Parent constructor called")

class Child(Parent):
    def __init__(self):
        super().__init__()  # cleaner way to call parent
        print("Child constructor called")

obj = Child()
#In Python, the super() method is used to call a method (usually __init__ or another function) from the parent (super) class.