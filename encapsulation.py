#1 Example
class Employee:
    def __init__(self, name):
        self.name = name   # public// __private// _protected 
    def display_name(self):   # public method
        print(self.name)

emp = Employee("Manoharan")
emp.display_name()  
print(emp.name)      

#2 Example:
class car:
    def __init__(self,brand):
        self.brand=brand
c = car("tata")
print(c.brand)

#3 Example
class Bank:
    def __init__(self):
        self.__balance=1000  #private attribute
    def get_balance(self):   #protected
        return self.__balance
    def show(self):
        return Bank.__get_balance(self)
b=Bank()
print(b.get_balance())     
print(b._Bank__balance)