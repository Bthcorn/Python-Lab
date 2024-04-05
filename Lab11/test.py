class Name:
    def __init__(self, title, first, last):
        self.title = title
        self.first = first
        self.last = last

    def get_full_name(self):
        return f"{self.title}. {self.first} {self.last}"


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_date(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    def get_date_bc(self):
        bc = self.year + 543
        return f"{self.day:02d}/{self.month:02d}/{bc}"


class Address:
    def __init__(self, house_no, street, district, city, country, postcode):
        self.house_no = house_no
        self.street = street
        self.district = district
        self.city = city
        self.country = country
        self.postcode = postcode

    def get_address(self):
        return f"{self.house_no}, {self.street}, {self.district}, {self.city}, {self.country}, {self.postcode}"


class Department:
    def __init__(self, description, manager, employee_list):
        self.description = description
        self.manager = manager
        self.employee_list = employee_list

    def add_employee(self, employee):
        self.employee_list.append(employee)
        employee.department = self.description

    def delete_employee(self, employee):
        self.employee_list.remove(employee)
        employee.department = ""

    def set_manager(self, employee):
        if employee in self.employee_list and hasattr(employee, "salary"):
            self.manager = employee

    def print_info(self):
        print("Department: %s" % self.description)
        print("Manager: %s" % self.manager.name.get_full_name())
        for employee in self.employee_list:
            print(employee.name.get_full_name())


class Person:
    def __init__(self, name, birth_date, address):
        self.name = name
        self.birth_date = birth_date
        self.address = address

    def print_info(self):
        print("Name: %s" % self.name.get_full_name())
        print("Birthdate: %s" % self.birth_date.get_date())
        print("Address: %s" % self.address.get_address())


class Employee(Person):
    def __init__(self, name, birth_date, address, start_date, department):
        super().__init__(name, birth_date, address)
        self.start_date = start_date
        self.department = department

    def print_info(self):
        super().print_info()
        print("Start Date: %s" % self.start_date.get_date())
        print("Department: %s" % self.department)



class TempEmployee(Employee):
    def __init__(self, name, birth_date, address, start_date, department, wage):
        super().__init__(name, birth_date, address, start_date, department)
        self.wage = wage

    def print_info(self):
        super().print_info()
        print("Wage: %s" % self.wage)


class PermEmployee(Employee):
    def __init__(self, name, birth_date, address, start_date, department, salary):
        super().__init__(name, birth_date, address, start_date, department)
        self.salary = salary

    def print_info(self):
        super().print_info()
        print("Salary: %s" % self.salary)


n1 = Name("Mr", "John", "Smith")
e1 = PermEmployee(
    n1,
    Date(1, 1, 1990),
    Address("1", "Street", "District", "City", "Country", "Postcode"),
    Date(1, 1, 2018),
    "",
    1000,
)
manager_name = e1
d = Department("IT", manager_name, [])

e2 = PermEmployee(
    Name("Mr", "Jay", "Som"),
    Date(1, 1, 1990),
    Address("1", "Street", "District", "City", "Country", "Postcode"),
    Date(1, 1, 2018),
    d,
    1000,
)

e3 = TempEmployee(
    Name("Mr", "Mike", "Soho"),
    Date(1, 1, 1990),
    Address("1", "Street", "District", "City", "Country", "Postcode"),
    Date(1, 1, 2018),
    "",
    1000,
)

d.add_employee(e2)
d.add_employee(e3)
d.set_manager(e2)
d.set_manager(e1)
d.set_manager(e3)
d.delete_employee(e2)
d.print_info()
e3.print_info()
