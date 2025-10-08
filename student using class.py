class student:
    def read(self,roll,name):
        self.roll=roll
        self.name=name
        print("student read")
    def write(self):
        print("student roll",self.roll)
        print("student name",self.name)
        print("student write")
s1=student()
s2=student()
s1.read(1,'mahi')
s1.write()
s2.read(2,'hari')
s2.write()