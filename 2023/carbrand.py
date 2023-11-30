from enum import Enum

class Brand(Enum):
    Mercedes = 1
    Audi = 2

class Type(Enum):
    Hatchback = 1
    Van = 2

class Car:
    def __init__(self, brand, doors, is_electric, cartype, color):
        self.brand = brand
        self.doors = doors
        self.is_electric = is_electric
        self.type = cartype
        self.color = color
    
    def print_car(self):
        print(self.brand, self.doors, "Doors, Is Electric?", self.is_electric, "Type:", self.type, self.color)

mercedes = Car("Mercedes", 4, False, "Hatchback", "White")
audi = Car("Audi", 2, True, "Van", "Gray")

mercedes.print_car()
audi.print_car()