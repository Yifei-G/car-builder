import abc


class Tires(abc.ABC):

    @abc.abstractmethod
    def get_pressure():
        pass

    @abc.abstractmethod
    def pump():
        pass
