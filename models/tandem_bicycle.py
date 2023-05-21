from models.abstract_bicycle import AbstractBicycle


class TandemBicycle(AbstractBicycle):
    def __init__(self, max_speed: int, current_speed: int, max_passengers_weight: int):
        super().__init__(max_speed, current_speed)

        self.max_passengers_weight = max_passengers_weight

    def get_max_distance(self):
        return self.max_passengers_weight * 20

    def __str__(self):
        return f"Tandem bicycle: \n\tMax passengers weight: {self.max_passengers_weight} ," \
               f",\n\tMax speed: {self.max_speed} \n" \
               f"\tCurrent speed: {self.current_speed} \n"
