class Employee:
    def __init__(self,name,hour_rate,hour_work):
        self.name=name
        self.hour_rate=hour_rate
        self.hour_work=hour_work
    def calc_salary(self):
        return self.hour_rate * self.hour_work


Employee=[
    Employee('mahi',500,40),
    Employee('mano',500,70),
    Employee('hari',500,30)
]
del Employee[1]
for emp in Employee:
    salary = emp.calc_salary()
    print(f"{emp.name}'s salary is ${salary}")