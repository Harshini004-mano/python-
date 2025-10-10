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

if __name__ == "__main__":
    v=vehicle("tata","bus")
    v.start()

    c=car("bense","lorry")
    c.start()
    c.playmusic()

    ele=electric_vechicle("lonova","tractor")
    ele.start()
    ele.playmusic()
    ele.charger()

    sma=smart_car("audi","racer car")
    sma.start()
    sma.playmusic()
    sma.connect_wifi()
    sma.auto_drive()

    b=bike("splender","enfiled")
    b.start()
    b.kick_start()

    elca=Electric_Smartcar("hundai","samsung")
    elca.start()
    elca.playmusic()
    elca.charger()
    elca.connect_wifi()
    elca.auto_drive()
    elca.autopilot_mode()