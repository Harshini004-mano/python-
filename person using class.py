class person:
    def read(self,name):
        self.name=name
    def greet(self):
        print(f" hi {self.name}")

p1=person()
p1.read('mahi')
p1.greet()
p2=person()
p2.read('hari')
p2.greet()