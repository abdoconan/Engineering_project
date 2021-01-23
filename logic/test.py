from Ceiling import Ceil
from Carpentry import Carpentry

if __name__ == "__main__":
    myCiel = Ceil(0, 150)
    temperaryDict = {
        "ceilingObj": myCiel,
        "woodenNailSixCmRate": 0.12,
        "woodenNailSixCmPrice": 16,
        "woodSawCylinderQuantity": 2,
        "woodSawCylinderPrice": 28,
        "dubbingRate": 0.0282667,
        "dubbingPrice": 25,
        "consumptionOfEquipmentRate": 0.00395,
        "consumptionOfEquipmentPrice": 31000,
        "consumptionOfBigToolsRate": 0.00987,
        "consumptionOfBigToolsPrice": 290000,
        "consumptionOfSmallToolsRate":0.03949,
        "consumptionOfSmallToolsPrice": 328000
    }
    myCarpentry = Carpentry(**temperaryDict)
    print(myCarpentry.totalOfCarpentryEquipmentAndToolsPerMeter())

