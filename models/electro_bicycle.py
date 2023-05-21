from models.abstract_bicycle import AbstractBicycle


class ElectroBicycle(AbstractBicycle):
    def __init__(self, max_speed: int, current_speed: int, battery_capacity: int, charge_per_100m: int):
        super().__init__(max_speed, current_speed)

        self.battery_capacity = battery_capacity
        self.charge_per_100m = charge_per_100m

    def get_max_distance(self):
        return self.battery_capacity / self.charge_per_100m

    def __str__(self):
        return f"Electro bicycle: \n\tCapacity: {self.battery_capacity} ,\n\tCharge per 100m: {self.charge_per_100m}" \
               f",\n\tMax speed: {self.max_speed} \n" \
               f"\tCurrent speed: {self.current_speed} \n"
