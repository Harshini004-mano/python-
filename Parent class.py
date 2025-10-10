# Parent class 
class MedicalDevice: 
    def __init__(self, device_name): 
        self.device_name = device_name 
 
    def switch_on(self): 
        print(f"{self.device_name} is now switched on.") 