import abc


class Engine(abc.ABC):

    @abc.abstractmethod
    def start():
        pass

    @abc.abstractmethod
    def stop():
        pass

    @abc.abstractmethod
    def get_state():
        pass
