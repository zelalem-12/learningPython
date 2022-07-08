from abc import ABC, abstractclassmethod

from more_itertools import last



class Employee(ABC):
    def __init__(self, firstName, lastName):
        self.firstName= firstName
        self.lastName= lastName

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    @abstractclassmethod
    def get_salary(self):
        pass