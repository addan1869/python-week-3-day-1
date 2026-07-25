class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)

s1 = Student("Ali", 101)
s1.display()