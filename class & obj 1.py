class Employee:

    def putdata(self, emp_no):

        self.emp_no = emp_no

        print("\nEnter the details of Employee", self.emp_no)

        self.name = input("Enter employee name: ")
        self.id = input("Enter employee ID: ")
        self.salary = input("Enter employee salary: ")
        self.department = input("Enter employee department: ")

    def displaydata(self):

        print("\nDetails of Employee", self.emp_no)
        print("Employee Name:", self.name)
        print("Employee ID:", self.id)
        print("Employee Salary:", self.salary)
        print("Employee Department:", self.department)



e1 = Employee()
e1.putdata("E1")

e2 = Employee()
e2.putdata("E2")

e3 = Employee()
e3.putdata("E3")

print("      Employee Records")
print("==============================")

e1.displaydata()
e2.displaydata()
e3.displaydata()