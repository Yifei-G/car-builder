from car_components.car_engine.engine import Engine


class Electric_Engine(Engine):

    def __init__(self, power):
        self.power = power

    def start(self):
        print("The electric engine is starting with power {}".format(self.power))

    def stop(self):
        print("The electric engine is stopping!")

    def get_state(self):
        print("The electric engine with power {} is working as expected".format(self.power))
