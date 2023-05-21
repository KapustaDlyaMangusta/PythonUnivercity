class Bicycle:
    instance = None

    """Class constructor"""

    def __init__(self, brand: str, bicycle_type: str, max_speed: int, current_speed: int):
        self.__brand = brand
        self.__bicycle_type = bicycle_type
        self.__max_speed = max_speed
        self.__current_speed = current_speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__brand = value

    @property
    def bicycle_type(self):
        return self.__bicycle_type

    @bicycle_type.setter
    def bicycle_type(self, value):
        self.__bicycle_type = value

    @property
    def max_speed(self):
        return self.__brand

    @max_speed.setter
    def max_speed(self, value):
        self.__max_speed = value

    @property
    def current_speed(self):
        return self.__brand

    @current_speed.setter
    def current_speed(self, value):
        self.__current_speed = value

    """Class methods"""

    def accelerate(self, speed):
        self.__current_speed = min(self.__max_speed, self.__current_speed + speed)

    def brake(self):
        self.__current_speed = 0

    def slow_down(self, speed):
        self.__current_speed = self.__current_speed - speed if self.__current_speed - speed >= 0 else 0

    """Implicit string casting overriding"""

    def __str__(self):
        print(
            f"Bicycle:"
            f"\n\tBrand: {self.__brand}"
            f",\n\tType: {self.__bicycle_type}"
            f",\n\tMax speed: {self.__max_speed}"
            f",\n\tCurrent speed: {self.__current_speed}"
            f"\n")

    """Singleton pattern implementation"""

    @staticmethod
    def get_instance():
        if not Bicycle.instance:
            Bicycle.instance = Bicycle(".",".",0,0)
            return Bicycle.instance

        return Bicycle.instance


if __name__ == '__main__':
    first = Bicycle("Brand", "Mountain", 100, 20)
    second = Bicycle.get_instance()
    items = [first, second]
    for item in items:
        print(item)
