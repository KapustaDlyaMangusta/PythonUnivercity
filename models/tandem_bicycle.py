from models.abstract_bicycle import AbstractBicycle


class TandemBicycle(AbstractBicycle):
    def __init__(self, max_speed: int, current_speed: int, possible_roads_set, max_passengers_weight: int):
        """Calling parent constructor"""
        super().__init__(max_speed, current_speed, possible_roads_set)

        """Initializing fields"""
        self.max_passengers_weight = max_passengers_weight

    def get_max_distance(self):
        """Return distance due to max passengers` weight"""
        return self.max_passengers_weight * 20

    def man_what_are_u_doing(self):
        pass

    def __str__(self):
        """To string method overriding"""
        return f"Tandem bicycle: \n\tMax passengers weight: {self.max_passengers_weight} ," \
               f",\n\tMax speed: {self.max_speed} \n" \
               f"\tCurrent speed: {self.current_speed} \n"
