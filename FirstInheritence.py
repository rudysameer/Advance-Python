class Vechile:
    def general_useage(self):
        self.fuel = "Petrol"
        print("I am an vechile\n")

class Car(Vechile):
    def __init__(self):
        print("I am an car")
        self.wheels = 4
        self.has_roof = True

    def specific_useage(self):
        print("Specific use for Family vacations,picnics and tours")

class Bike(Vechile):
    def __init__(self):
        print("I am an Bike")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print("Specific use for offroad riding and Day to day office use") 

c = Car()
c.specific_useage()
c.general_useage()
print("The having roof is ",c.has_roof)
print("The number of the wheels is",c.wheels)
print("Runs on ",c.fuel)


b = Bike()
b.specific_usage()
b.general_useage()
print("The roof is ",b.has_roof)
print("The wheels it has is ",b.wheels)
print("runs on ",b.fuel)
print("\n")
print(isinstance(b,Bike))
print(isinstance(b,Car))
print(issubclass(Car,Vechile))
print(issubclass(Car,Bike))