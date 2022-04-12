"""
Assignment name: Multiple Inheritance
Program: Employee.py
Author: Colby Boell
Last date modified: 04/03/2022

The purpose of this program is to use classes to create multiple inheritance for the manager class because
they are a person and and employee
"""
# import
from datetime import datetime



# Employee class
class Employee:
    def __init__(self, start_date, salary):
        dateformat = datetime.strptime(start_date, '%m-%d-%Y')
        self.start_date = dateformat.strftime('%m-%d-%Y')
        self.salary = salary

    def give_raise(self, salary):
        self.salary = salary

    def display(self):
        return f'{self.start_date}\nSalary: ${str(self.salary)}/year'
