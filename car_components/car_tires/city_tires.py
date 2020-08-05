from car_components.car_tires.tires import Tires


class City_Tires(Tires):

    def __init__(self, size):
        self.size = size
        self.pressure = 32

    def get_pressure(self):
        print("The pressure of the city tires is: {} PSI".format(self.pressure))

    def pump(self):
        print("The city tires with size {} is pumping...".format(self.size))
