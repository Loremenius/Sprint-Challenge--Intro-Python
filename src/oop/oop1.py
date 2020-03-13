# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle():
    def __init__(self):
        self.vehicle = "Its a vehicle"

class FlightVehicle(Vehicle):
    def __init__(self):
        self.flight_vehivle = "It can fly!"
        super().__init__()

class Starship(FlightVehicle):
    def __init__(self):
        self.starship = "Its a space ship"
        super().__init__()

class GroundVehicle(Vehicle):
    def __init__(self):
        self.ground_vehicle = "Its a vehicle for the ground"
        super().__init__()

class Car(GroundVehicle):
    def __init__(self):
        self.ground_vehicle = "Its a car"
        super().__init__()

class Motorcycle(GroundVehicle):
    def __init__(self):
        self.ground_vehicle = "Its a motorcycle"
        super().__init__()

class Airplane(FlightVehicle):
    def __init__(self):
        self.ground_vehicle = "Its an airplane"
        super().__init__()