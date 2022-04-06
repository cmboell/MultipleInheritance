from class_definitions.Employee import Employee
from class_definitions.Person import Person


class Manager(Person, Employee):
    def __init__(self, last_name, first_name, address, phone_number, start_date, salary):
        super().__init__(last_name, first_name, address, phone_number, start_date, salary)

    def display(self):
        return f'{self.first_name}'


# Driver
if __name__ == "__main__":
    m = Manager('Boell', 'Colby', '123 N.Main St.\nTown, IA 12345', '111-222-3333', '02-20-2020', 40000.00)
    print(m.display())
