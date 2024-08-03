from patterns_01_3_0_cars import *
from patterns_01_3_1_cars import *
from patterns_01_3_2_cars import *


abstract_transport = Transport(Engine, Driver)
electric_robot_truck = Truck(ElectricEngine, Robot)
combustion_human_car = Car(CombustionEngine, Human)