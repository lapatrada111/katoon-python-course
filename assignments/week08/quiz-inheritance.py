""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class vehicle:

    def __init__ (brand, model, year):
        self.model = brand
        self.model = model
        seaf.year = year

    def get_info(self):
        seturn f"Brand": {self.brand},Model:{self.model}, Y

class car(Vehicle):
    def __init__ (self,brand, model, year):
        super() __init__ (brand, model, year):
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"Brand": {self.brand},Model:{self.model}, Y
