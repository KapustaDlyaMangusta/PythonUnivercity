import sys

from models.abstract_bicycle import AbstractBicycle


class Bicycle(AbstractBicycle):
    def __init__(self,  max_speed: int, current_speed: int, brand: str, bicycle_type: str):
        super().__init__(max_speed, current_speed)

        self.brand = brand
        self.bicycle_type = bicycle_type

    def accelerate(self, speed):
        self.current_speed = min(self.max_speed, self.current_speed + speed)

    def brake(self):
        self.current_speed = 0

    def slow_down(self, speed):
        self.current_speed = self.current_speed - speed if self.current_speed - speed >= 0 else 0

    def get_max_distance(self):
        return sys.maxsize

    def __str__(self):
        return f"Bicycle: \n\tBrand: {self.brand} ,\n\tType: {self.bicycle_type} ,\n\tMax speed: {self.max_speed} \n" \
               f"\tCurrent speed: {self.current_speed} \n"
