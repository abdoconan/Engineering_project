class Ceil(object):
    def __init__(self, floorNumber, sizeInMeterQuebed = 1):
        assert((type(floorNumber) == int or type(floorNumber) == float) and  floorNumber >= 0), "can't have the floor number to be less than basement"
        assert(type(sizeInMeterQuebed) == int and sizeInMeterQuebed > 0 ), "can't have size with 0 or less meter"
        self.floorNumber = floorNumber
        self.sizeInMeterQuebed = sizeInMeterQuebed
    
    def __str__(self):
        return (f"this is ceiling for the {self.trasformFloor()} with total space is {self.sizeInMeterQuebed} m\u00b3")

    def trasformFloor(self):
        if (self.floorNumber == 0):
            return "basement"
        if (self.floorNumber == 1):
            return "first floor"
        if (self.floorNumber == 2):
            return "second floor"
        if (self.floorNumber == 3):
            return "third floor"


