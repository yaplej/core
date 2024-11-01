from enum import Enum

from functools import partial

def vertial_20lb(tank_level:int):
    print("Function to calculate volume of vertial 20 lb tank from tank_level")

def vertial_30lb(tank_level:int):
    print("Function to calculate volume of vertial 30 lb tank from tank_level")

def vertial_40lb(tank_level:int):
    print("Function to calculate volume of vertial 40 lb tank from tank_level")

def vertial_100gal(tank_level:int):
    print("Function to calculate volume of vertial 100 gallon tank from tank_level")

def vertial_120gal(tank_level:int):
    print("Function to calculate volume of vertial 120 gallon tank from tank_level")

def horizontal_120gal(tank_level:int):
    print("Function to calculate volume of horizontal 120 gallon tank from tank_level")

def horizontal_150gal(tank_level:int):
    print("Function to calculate volume of horizontal 150 gallon tank from tank_level")

def horizontal_250gal(tank_level:int):
    print("Function to calculate volume of horizontal 250 gallon tank from tank_level")

def horizontal_500gal(tank_level:int):
    print("Function to calculate volume of horizontal 500 gallon tank from tank_level")

def horizontal_1000gal(tank_level:int):
    print("Function to calculate volume of horizontal 1000 gallon tank from tank_level")

class TankSize(Enum):
    VERTICAL_20_LB = partial(vertial_20lb)
    VERTICAL_30_LB = partial(vertial_30lb)
    VERTICAL_40_LB = partial(vertial_40lb)
    VERTICAL_100_GAL = partial(vertial_100gal)
    VERTICAL_120_GAL = partial(vertial_120gal)
    HORIZONTAL_120_GAL = partial(horizontal_120gal)
    HORIZONTAL_150_GAL = partial(horizontal_150gal)
    HORIZONTAL_250_GAL = partial(horizontal_250gal)
    HORIZONTAL_500_GAL = partial(horizontal_500gal)
    HORIZONTAL_1000_GAL = partial(horizontal_1000gal)
