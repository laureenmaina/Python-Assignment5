class Vehicle:
    def move(self):
        pass 

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Instances of the classes
car = Car()
plane = Plane()
boat = Boat()

# Method for each instance
car.move()
plane.move()
boat.move()