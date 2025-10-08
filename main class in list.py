class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"hi {self.name}")

if __name__=="__main__":
   Human =[
       person("mahi"),
       person("hari"),
       person("mano")
       ]
for per in Human:
    print(f"{per.name}")
 