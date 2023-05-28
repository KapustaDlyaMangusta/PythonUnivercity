class BicycleManager:
    def __init__(self):
        self.bicycles = []

    def add_bicycle(self, bicycle):
        self.bicycles.append(bicycle)

    def get_bicycles_faster_than(self, speed):
        return [bicycle for bicycle in self.bicycles if bicycle.max_speed > speed]

    def get_bicycle_by_id(self, bicycle_id):
        for bicycle in self.bicycles:
            if bicycle.bicycle_id == bicycle_id:
                return bicycle
        return None
