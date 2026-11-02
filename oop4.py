#inheritance
from encodings import cp1006


# employees -- name, id, department, gender
# salaried --  +  salary, tenure
# casual  --  rates
class Employee:
    def __init__(self, name:str, id_no:str, department:str, gender:str):
        self.name = name
        self.id_no = id_no
        self.department = department
        self.gender = gender
    def print_employee_info(self):
        print(self.name)
        print(self.id_no)
        print(self.department)
        print(self.gender)
        if hasattr(self, "salary"):
            print(self.salary)
        if hasattr(self, "tenure"):
            print(self.tenure)
        if hasattr(self, "rate"):
            print(self.rate)
        print("-----------------------------")
    def print_name(self):
        print(f"Name is: {self.name}")
class salariedEmployee(Employee):
     def __init__(self, name:str, id_no:str, department:str, gender:str, tenure, salary:float):
         super().__init__(name, id_no, department, gender)
         self.tenure = tenure
         self.salary = salary

class CasualWorkers(Employee):
    def __init__(self, name: str, id_no: str, department: str, gender: str, rate: float):
        super().__init__(name, id_no, department, gender)
        self.rate = rate
    def calc_wages(self, hours_worked: float):
        return self.rate * hours_worked


s1 = salariedEmployee("Sarang Guen", "234756", "Construction", "Male", 5, 95000)
c2 = CasualWorkers(name="jack onyango", id_no="234756", department="Construction", gender="Male", rate=465.00)

s1.print_employee_info()
c2.print_employee_info()
print("Wages for casual worker: ", c2.calc_wages(23))

s1.print_name()