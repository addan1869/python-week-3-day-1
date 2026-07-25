class Employee:

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Department:", self.department)

e1 = Employee("Ali", "IT")
e2 = Employee("Ahmed", "HR")
e3 = Employee("Sara", "Finance")

e1.display()
print()

e2.display()
print()

e3.display()