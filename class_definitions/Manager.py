from class_definitions.Employee import Employee
from class_definitions.Person import Person


class Manager(Person, Employee):
    def __init__(self, last_name, first_name, address, phone_number, start_date, salary, department, direct_reports=''):
        Person.__init__(self,last_name, first_name, address, phone_number)
        Employee.__init__(self, start_date, salary)
        self.department = department
        self.direct_reports = direct_reports

    def give_rase(self, salary):
        self.salary = salary

    def display(self):
        return f'Employee: {str(self.first_name)} {str(self.last_name)}\nAddress: {str(self.address)}\n' \
               f'Phone: {str(self.phone_number)}\nStart Date:{self.start_date}\n' \
               f'Salary: ${float(self.salary)}/year\nDepartment: {str(self.department)}\n' \
               f'Direct Reports: {list(self.direct_reports)}'


# Driver
if __name__ == "__main__":
    m = Manager('Boell', 'Colby', '123 N.Main St.\nTown, IA 12345', '111-222-3333', '03-05-2022', 40000.00, 'Logistics')
    print(m.display())

