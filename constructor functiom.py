class person:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f" hi {self.name}")

p1=person("mahi")
p1.greet()
p2=person("hari")
p2.greet()
