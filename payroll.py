class Payroll:
    def __init__(self):
        self.employeeList=[]
    
    def add(self, employee):
        self.employeeList.append(employee)
    
    def print(self):
        for employee in self.employeeList:
            print(f"{employee.fullName} \t ${employee.get_salary()}")