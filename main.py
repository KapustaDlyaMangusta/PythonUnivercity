from managers.bicycle_manager import BicycleManager
from managers.bicycle_set_manager import BicycleSetManager
from models.bicycle import Bicycle
from models.electro_bicycle import ElectroBicycle
from models.kid_bicycle import KidBicycle
from models.tandem_bicycle import TandemBicycle

if __name__ == '__main__':
    bicycle_manager = BicycleManager()

    bicycle_list = [
        ElectroBicycle(40, 20, {"Mountain", "City"}, 12000, 100),
        ElectroBicycle(60, 50, {"Mountain", "City", "Sea"}, 15000, 80),
        Bicycle(45, 30, {"Road", "Alaska"}, "Mountain", "Mercedes"),
        Bicycle(50, 20, {"Mountain", "Ryasne"}, "Road", "Daewoo Matiz"),
        KidBicycle(12, 43, {"Volcano", "City"}, 5, 4),
        KidBicycle(30, 12, {"Volcano", "Buildings"}, 8, 3),
        TandemBicycle(10, 100, {"Mountain", "Columbia"}, 30),
        TandemBicycle(180, 185, {"Columbia"}, 130)
    ]

    for bicycle in bicycle_list:
        bicycle_manager.add_bicycle(bicycle)

    for bicycle in bicycle_manager.bicycles:
        print(bicycle)

    print("\n Faster than: \n")

    fast_bicycles = bicycle_manager.get_bicycles_faster_than(60)

    for bicycle in fast_bicycles:
        print(bicycle)

    print("\nMax distances: \n")

    all_bicycles = bicycle_manager.get_bicycles_max_distance()

    for bicycle in all_bicycles:
        print(bicycle)

    print("\nBy id: \n")

    bicycle = bicycle_manager.get_bicycle_by_id(2)
    print(bicycle)

    print("\nEnumeration: \n")

    bicycles_enumeration = bicycle_manager.get_bicycles_enumeration()

    for index, bicycle in bicycles_enumeration:
        print(index, bicycle)

    print("\nBicycles zip by max distance: \n")

    bicycles_zip_by_max_distance = bicycle_manager.get_bicycles_zip_by_max_distance()

    for bicycle, max_distance in bicycles_zip_by_max_distance:
        print(f"{type(bicycle).__name__} with id - {bicycle.bicycle_id}: {max_distance}")

    print("\nList of tuples of bicycles integer attributes: \n")

    bicycles_attributes_by_type = bicycle_manager.get_bicycles_attributes_by_type(int)

    for bicycle_attributes_by_type in bicycles_attributes_by_type:
        print(bicycle_attributes_by_type)

    print("\nCondition check: \n")

    print(bicycle_manager.check_bicycles_on_condition(lambda bicycle_item: bicycle_item.max_speed > 20))

    bicycle_set_manager = BicycleSetManager(bicycle_manager)

    print("\nSet manager iteration: \n")

    for bicycle_set_value in bicycle_set_manager:
        print(bicycle_set_value)

    print("\nSet manager length: \n")

    print(len(bicycle_set_manager))

    for exception_bicycle_demonstrator in bicycle_manager.bicycles:
        exception_bicycle_demonstrator.man_what_are_u_doing()
