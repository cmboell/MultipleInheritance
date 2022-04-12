"""
Assignment name: Multiple Inheritance
Program: Employee.py
Author: Colby Boell
Last date modified: 04/03/2022

The purpose of this program is to use classes to create multiple inheritance for the manager class because
they are a person and and employee
"""
# person class
class Person:
    def __init__(self, last_name, first_name, address='', phone_number=''):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number

    def display(self):
        return f'{str(self.first_name)} {str(self.last_name)}\n{str(self.address)}\n{str(self.phone_number)}'
