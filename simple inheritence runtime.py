#parent class
class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand}  {self.model} is starting.")

class car(vehicle):
    def playmusic(self):
        print(f"{self.brand} {self.model} is playing music.")

class electric_vechicle(car):
    def charger(self):
        print(f"{self.brand} {self.model} is charging.")

class smart_device:
     def connect_wifi(self):
        print("WIFI connected.")

class smart_car(car,smart_device):
    def auto_drive(self):
        print(f"{self.brand} {self.model} is automatic mode.")

class bike(vehicle):
    def kick_start(self):
        print(f"{self.brand} {self.model} is kick start model.")
    
class Electric_Smartcar (smart_car,electric_vechicle):
    def autopilot_mode(self):
        print(f"{self.brand} {self.model} is autopilot mode.")

def main():
    print("^^^ Vehicle System ^^^")
    print("Choose vehicle type:")
    print("1. Vehicle\n2. Car\n3. Electric Vehicle\n4. Smart Car\n5. Bike\n6. Electric Smart Car")

    choice = input("Enter the choice= ")
    brand = input("Enter the brand: ")
    model = input("Enter the model: ")

    if choice == "1":
       v=vehicle(vehicle,model)
       v.start()

    elif choice == "2":
         c=car(vehicle,model)
         c.start()
         c.playmusic()

    elif choice == "3":
         ele=electric_vechicle(vehicle,model)
         ele.start()
         ele.playmusic()
         ele.charger()

    elif choice == "4":
         sma=smart_car(vehicle,model)
         sma.start()
         sma.playmusic()
         sma.connect_wifi()
         sma.auto_drive()

    elif choice == "5":
         b=bike(vehicle,model)
         b.start()
         b.kick_start()

    elif choice == "6":
         elca=Electric_Smartcar(vehicle,model)
         elca.start()
         elca.playmusic()
         elca.charger()
         elca.connect_wifi()
         elca.auto_drive()
         elca.autopilot_mode()
 
    else :
         print("Invalid")

if __name__ == "__main__":
    main()