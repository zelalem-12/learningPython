from employee import Employee

class HourlyEmployee(Employee):
    def __init__(self, firstName, lastName, workedHours, rate):
        super().__init__(firstName, lastName)
        self.workedHours= workedHours
        self.rate= rate


    def get_salary(self):
        return self.workedHours * self.rate