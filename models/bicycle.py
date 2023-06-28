"""Module for Bicycle class"""

import sys

from decorators.logger import logger
from exceptions.man_what_are_you_doing import ManWhatAreUDoingException
from models.abstract_bicycle import AbstractBicycle


class Bicycle(AbstractBicycle):
    """Methods for class"""

    def __init__(self,  max_speed: int, current_speed: int,
                 possible_roads_set, brand: str, bicycle_type: str):
        """Calling parent constructor"""
        super().__init__(max_speed, current_speed, possible_roads_set)

        self.brand = brand
        self.bicycle_type = bicycle_type

    def accelerate(self, speed):
        """Increasing current speed for given value, but not more than max"""
        self.current_speed = min(self.max_speed, self.current_speed + speed)

    def brake(self):
        """Setting current speed value to zero"""
        self.current_speed = 0

    def slow_down(self, speed):
        """Decreasing current speed by value, but not less than 0"""
        self.current_speed = self.current_speed - speed if self.current_speed - speed >= 0 else 0

    def get_max_distance(self):
        """Returning something default, because common bicycle is immortal"""
        return sys.maxsize

    @logger(ManWhatAreUDoingException, "file")
    def man_what_are_u_doing(self):
        raise ManWhatAreUDoingException("Man, what are u doing?")

    def __str__(self):
        """To string method overriding"""
        return f"Bicycle: \n\tBrand: {self.brand} ,\n\tType: {self.bicycle_type} ,\n\tMax speed: {self.max_speed} \n" \
               f"\tCurrent speed: {self.current_speed} \n"
