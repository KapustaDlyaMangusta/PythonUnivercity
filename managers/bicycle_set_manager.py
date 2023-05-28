from managers.bicycle_manager import BicycleManager
from models.bicycle import Bicycle


class BicycleSetManager:
    def __init__(self, bicycle_manager: BicycleManager):
        self.bicycle_manager = bicycle_manager
        self.possible_roads_iterator = None
        self.current_bicycle: Bicycle = None
        self.bicycle_manager_iterator = iter(bicycle_manager)

    def __iter__(self):
        return self

    def __len__(self):
        return sum(len(bicycle.possible_roads_set) for bicycle in self.bicycle_manager)

    def __getitem__(self, index):
        for bicycle in self.bicycle_manager:
            if index < len(bicycle.possible_roads_set):
                return list(bicycle.possible_roads_set)[index]
            index -= len(bicycle.possible_roads_set)
        raise IndexError("Index out of range")

    def __next__(self):
        if self.current_bicycle is None or self.possible_roads_iterator is None:
            self.current_bicycle = next(self.bicycle_manager_iterator)
            self.possible_roads_iterator = iter(self.current_bicycle.possible_roads_set)

        try:
            return next(self.possible_roads_iterator)
        except StopIteration:
            self.current_bicycle = next(self.bicycle_manager_iterator)
            self.possible_roads_iterator = iter(self.current_bicycle.possible_roads_set)
            return next(self.possible_roads_iterator)
