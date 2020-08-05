from car_components.car_tires.city_tires import City_Tires
from car_components.car_tires.offroad_tires import Offroad_Tires
from car_components.car_engine.electric_engine import Electric_Engine
from car_components.car_engine.petrol_engine import Petrol_Engine
from cars.car import Car

print("Creating a city car!")
my_city_car = Car("Ex12304", Electric_Engine(25), City_Tires(15))

my_city_car.engine.get_state()
my_city_car.tires.pump()

print("Creating a mountain car!")
my_mountain_car = Car("HQ3594", Petrol_Engine(54), Offroad_Tires(18))

my_mountain_car.engine.get_state()
my_mountain_car.tires.pump()
print("Changing the mountain car engine!")
my_mountain_car.engine = Electric_Engine(54)
my_mountain_car.engine.get_state()
