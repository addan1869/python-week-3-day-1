class Rectangle:

    def area(self, length, width):
        print("Area =", length * width)

r1 = Rectangle()

length = int(input("Enter Length: "))
width = int(input("Enter Width: "))

r1.area(length, width)