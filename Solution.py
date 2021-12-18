class Circle:
    radius = int(input("Enter Radius : "))
    pass

    def area(self):
        return 3.1416*(Circle.radius ** 2)


cir = Circle()
print("Area of Circle :", cir.area())
