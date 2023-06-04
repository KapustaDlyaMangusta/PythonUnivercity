from models.abstract_bicycle import AbstractBicycle


class ElectroBicycle(AbstractBicycle):
    def __init__(self, max_speed: int, current_speed: int, possible_roads_set, battery_capacity: int, charge_per_100m: int):
        """Calling parent constructor"""
        super().__init__(max_speed, current_speed, possible_roads_set)

        """Initializing fields"""
        self.battery_capacity = battery_capacity
        self.charge_per_100m = charge_per_100m

    def get_max_distance(self):
        """Returns distance due to capacity and charge per 100m"""
        return self.battery_capacity / self.charge_per_100m

    def __str__(self):
        """To string method overriding"""
        return f"Electro bicycle: \n\tCapacity: {self.battery_capacity} ,\n\tCharge per 100m: {self.charge_per_100m}" \
               f",\n\tMax speed: {self.max_speed} \n" \
               f"\tCurrent speed: {self.current_speed} \n"
