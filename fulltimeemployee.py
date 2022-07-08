from employee import Employee

class FullTimeEmployee(Employee):
    def __init__(self, firstName, lastName, salary):
        super().__init__(firstName, lastName)
        self.salary= salary


    def get_salary(self):
        return self.salary 