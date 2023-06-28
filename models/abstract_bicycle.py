"""Module for abstract classes that dedicated to bicycle"""

import abc


class AbstractBicycle(abc.ABC):
    """Global id for all nested classes"""
    global_id: int = 0

    def __init__(self, max_speed: int, current_speed: int, possible_roads_set):
        """Contructor
        :param: max_speed - max speed for bicycle
        :param: current_speed - current speed of bicycle
        :param: possible_roads_set - set of all roads that can bicycle ride"""
        AbstractBicycle.global_id += 1

        self.max_speed = max_speed
        self.current_speed = current_speed
        self.bicycle_id = AbstractBicycle.global_id
        self.possible_roads_set = possible_roads_set

    @abc.abstractmethod
    def get_max_distance(self):
        """Absract method for getting max distance"""
