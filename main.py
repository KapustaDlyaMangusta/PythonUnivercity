from managers.bicycle_manager import BicycleManager
from models.bicycle import Bicycle
from models.electro_bicycle import ElectroBicycle
from models.kid_bicycle import KidBicycle
from models.tandem_bicycle import TandemBicycle

if __name__ == '__main__':
    bicycleManager = BicycleManager()

    bicycleList = [
        ElectroBicycle(40, 20, 12000, 100),
        ElectroBicycle(60, 50, 15000, 80),
        Bicycle(45, 30,"Mountain", "Mercedes"),
        Bicycle(50, 20,"Road", "Daewoo Matiz"),
        KidBicycle(12, 43, 5, 4),
        KidBicycle(30, 12, 8, 3),
        TandemBicycle(10, 100, 30),
        TandemBicycle(180, 185, 130)
    ]

    for bicycle in bicycleList:
        bicycleManager.add_bicycle(bicycle)

    for bicycle in bicycleManager.bicycles:
        print(bicycle)

    print("\n Faster than: \n")

    fastBicycles = bicycleManager.get_bicycles_faster_than(60)

    for bicycle in fastBicycles:
        print(bicycle)

    print("\n By id: \n")

    bicycle = bicycleManager.get_bicycle_by_id(2)
    print(bicycle)
