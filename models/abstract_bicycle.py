class AbstractBicycle:
    global_id:int = 0

    def __init__(self, max_speed: int, current_speed: int):
        AbstractBicycle.global_id += 1

        self.max_speed = max_speed
        self.current_speed = current_speed
        self.bicycle_id = AbstractBicycle.global_id

    def get_max_distance(self):
        pass
