class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World!! Welcome to Car")

class PickUp(Vehicle):
    def sayHello(self):
        print("Hello World!! Welcome to PickUp")

class Van(Vehicle):
    def sayHello(self):
        print("Hello World!! Welcome to Van")

class EstrateCar(Vehicle):
    def sayHello(self):
        print("Hello World!! Welcome to EstrateCar")

car1 = Car()
car1.turnOnAirConditioner()

pickUp1 = PickUp()
pickUp1.turnOnAirConditioner()

van1 = Van()
van1.turnOnAirConditioner()

estrate1 = EstrateCar()
estrate1.turnOnAirConditioner()