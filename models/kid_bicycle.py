from models.abstract_bicycle import AbstractBicycle


class KidBicycle(AbstractBicycle):
    def __init__(self, max_speed: int, current_speed: int, possible_roads_set, recommended_age: int, wheels_count: int):
        """Calling parent constructor"""
        super().__init__(max_speed, current_speed, possible_roads_set)

        """Initializing fields"""
        self.recommended_age = recommended_age
        self.wheels_count = wheels_count

    def get_max_distance(self):
        """Returns distance due to age"""
        return self.recommended_age % 3 * 10

    def __str__(self):
        """To string method overriding"""
        return f"Kid bicycle: \n\tRecommended age: {self.recommended_age} ,\n\tWheels count: {self.wheels_count}" \
               f",\n\tMax speed: {self.max_speed} \n" \
               f"\tCurrent speed: {self.current_speed} \n"
