from models.abstract_bicycle import AbstractBicycle


class KidBicycle(AbstractBicycle):
    def __init__(self, max_speed: int, current_speed: int, recommended_age: int, wheels_count: int):
        super().__init__(max_speed, current_speed)

        self.recommended_age = recommended_age
        self.wheels_count = wheels_count

    def get_max_distance(self):
        return self.recommended_age % 3 * 10

    def __str__(self):
        return f"Kid bicycle: \n\tRecommended age: {self.recommended_age} ,\n\tWheels count: {self.wheels_count}" \
               f",\n\tMax speed: {self.max_speed} \n" \
               f"\tCurrent speed: {self.current_speed} \n"
