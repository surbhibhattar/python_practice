class Employee:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def display(self):
        print(f"Employee id: {self.id}\nname:{self.name}")


emp = Employee(1,"surbhi")
emp.display()
del emp.id
try:
    print(emp.id)
except NameError:
    print("emp.id not defined")
del emp
try:
    emp.display()
except NameError:
    print("emp not defined")


