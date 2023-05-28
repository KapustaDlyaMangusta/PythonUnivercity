class BicycleManager:
    def __init__(self):
        """Initializing array"""

        self.bicycles = []

    def __len__(self):
        """Returns the length of items in bicycles"""

        return len(self.bicycles)

    def __iter__(self):
        """Returns the iterator object for bicycles"""

        return iter(self.bicycles)

    def __getitem__(self, item):
        """Returns an item from bicycles by index"""

        return self.bicycles[item]

    def add_bicycle(self, bicycle):
        """Adding new bicycle to array"""

        self.bicycles.append(bicycle)

    def get_bicycles_faster_than(self, speed):
        """Getting list of bicycles that are faster than given speed"""

        return filter(lambda bicycle: bicycle.max_speed > speed, self.bicycles)

    def get_bicycle_by_id(self, bicycle_id):
        """Getting bicycle from list or raising exception if it does not exist"""

        try:
            return next(filter(lambda bicycle: bicycle.bicycle_id == bicycle_id, self.bicycles))
        except StopIteration:
            raise Exception("There is no such bicycle")

    def get_bicycles_max_distance(self):
        """Returns max distances of all bicycles"""

        return [bicycle.get_max_distance() for bicycle in self.bicycles]

    def get_bicycles_enumeration(self):
        """Returns enumeration of bicycles"""

        return enumerate(self.bicycles)

    def get_bicycles_zip_by_max_distance(self):
        """Returns zip of bicycles by max distance"""

        return zip(self.bicycles, self.get_bicycles_max_distance())

    def get_bicycles_attributes_by_type(self, data_type):
        """Returns list of tuples of bicycles attributes by given datatype"""

        return [{key: value for key, value in bicycle.__dict__.items() if isinstance(value, data_type)}
                for bicycle in self.bicycles]

    def check_bicycles_on_condition(self, condition):
        return {"all": all(condition(bicycle) for bicycle in self.bicycles),
                "any": any(condition(bicycle) for bicycle in self.bicycles)}
