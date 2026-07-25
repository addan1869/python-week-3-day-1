class Student:

    def getmarks(self):
        self.name = input("Enter Student Name: ")
        self.marks = int(input("Enter Marks: "))

    def result(self):
        if self.marks >= 50:
            print(self.name, "Pass")
        else:
            print(self.name, "Fail")

s1 = Student()
s1.getmarks()
s1.result()