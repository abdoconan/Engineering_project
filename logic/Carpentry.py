# from Ceiling import Ceil

class Carpentry(object):
    def __init__(self, ceilingObj, woodenNailSixCmRate = 0.01, woodenNailSixCmPrice = 0.01, woodSawCylinderQuantity = 0, woodSawCylinderPrice = 0.01, dubbingRate = 0.01, dubbingPrice = 0.01, consumptionOfEquipmentRate = 0.01, consumptionOfEquipmentPrice = 0.01, consumptionOfBigToolsRate = 0.01,  consumptionOfBigToolsPrice = 0.01, consumptionOfSmallToolsRate = 0.01, consumptionOfSmallToolsPrice = 0.01):
        self.ceilingObj = ceilingObj #السقف
        self.woodenNailSixCmRate = woodenNailSixCmRate #معدل مسامير 6 سم خشابي
        self.woodenNailSixCmPrice = woodenNailSixCmPrice #سعر مسامير 6 سم خشابي
        self.woodSawCylinderQuantity =woodSawCylinderQuantity #عدد اسطوانة منشار خشب
        self.woodSawCylinderPrice =woodSawCylinderPrice # سعر اسطوانة منشار خشب
        self.dubbingRate = dubbingRate # معدل دبلاج
        self.dubbingPrice = dubbingPrice # سعر دبلاج
        self.consumptionOfEquipmentRate = consumptionOfEquipmentRate #نسبة ستهلاك العدة والمعدات
        self.consumptionOfEquipmentPrice = consumptionOfEquipmentPrice # سعر ستهلاك العدة والمعدات
        self.consumptionOfBigToolsRate = consumptionOfBigToolsRate # نسية استهلاك العدة "العروق + الموسكيات"
        self.consumptionOfBigToolsPrice = consumptionOfBigToolsPrice # سعر استهلاك العدة "العروق + الموسكيات"
        self.consumptionOfSmallToolsRate = consumptionOfSmallToolsRate # نسبة استهلاك العدة "اللتزانة"
        self.consumptionOfSmallToolsPrice = consumptionOfSmallToolsPrice # سعر استهلاك العدة "اللتزانة"
        self.assertion()

    def assertion(self):
        # assert(type(self.ceilingObj) == Ceil.__class__()), "missing value of type ceiling"
        assert((type(self.woodenNailSixCmRate)== float) and (self.woodenNailSixCmRate > 0)), "nail rate has problem"
        assert((type(self.woodenNailSixCmPrice)== int or type(self.woodenNailSixCmPrice)==float) and self.woodenNailSixCmPrice > 0), "nail price has problem"
        assert((type(self.woodSawCylinderQuantity) == int) and (self.woodSawCylinderQuantity >= 0)), "wood saw Cylinder quantity has problem"
        assert((type(self.woodSawCylinderPrice) == int or type(self.woodSawCylinderPrice)== float) and self.woodSawCylinderPrice > 0), "wood saw Cylinder price has problem"
        assert(type(self.dubbingRate) == float and self.dubbingRate >0), "dubbing rate has problem"
        assert((type(self.dubbingPrice)== int or type(self.dubbingPrice) == float) and self.dubbingPrice > 0), "dubbing price has problem"
        assert(type(self.consumptionOfEquipmentRate)== float and self.consumptionOfEquipmentRate >= 0), "equitpment rate has problem"
        assert((type(self.consumptionOfEquipmentPrice)== int or type(self.consumptionOfEquipmentPrice)==float) and self.consumptionOfEquipmentPrice >= 0), "equitpment price has problem"
        assert(type(self.consumptionOfBigToolsRate)== float and self.consumptionOfBigToolsRate >= 0), "big tools rate has problem"
        assert((type(self.consumptionOfBigToolsPrice) == int or type(self.consumptionOfBigToolsPrice) == float) and self.consumptionOfBigToolsPrice >= 0), "big tools price has problem"
        assert(type(self.consumptionOfSmallToolsRate)== float and self.consumptionOfSmallToolsRate >= 0), "small tools rate has problem"
        assert((type(self.consumptionOfSmallToolsPrice)==int or type(self.consumptionOfSmallToolsPrice)== float) and self.consumptionOfSmallToolsPrice >= 0), "small tools price has problem"
    
    def quantityOfNielsNeeded(self): # كمية مسامير 6 سم خشابي
        return self.ceilingObj.sizeInMeterQuebed * self.woodenNailSixCmRate

    def priceOfNielsNeeded(self): # سعر مسامير 6 سم خشابي
        return self.quantityOfNielsNeeded() * self.woodenNailSixCmPrice
    def priceofWoodSawCylinderNeeded(self): #اسطوانة منشار خشب
        return self.woodSawCylinderQuantity * self.woodSawCylinderPrice
    def quantityOfDubbing(self): #كمية دبلاج
        return self.ceilingObj.sizeInMeterQuebed * self.dubbingRate
    def priceOFDubbing(self): # سعر دبلاج 
        return self.quantityOfDubbing() * self.dubbingPrice
    def totalOfCarpentryWoods(self): # احمالى اسعار الخشب
        return self.priceOfNielsNeeded() + self.priceofWoodSawCylinderNeeded() + self.priceOFDubbing()
    def priceOfEquipment(self): # سعر المعدات
        return self.consumptionOfEquipmentRate * self.consumptionOfEquipmentPrice
    def priceOfBigTools(self): # سعر استهلاك العدة "العروق + الموسكيات"
        return self.consumptionOfBigToolsRate * self.consumptionOfBigToolsPrice
    def priceOfSmallTools(self): # سعر استهلاك العدة "اللتزانة"
        return self.consumptionOfSmallToolsRate * self.consumptionOfSmallToolsPrice
    def totalOfCarpentryEquipmentAndTools(self): # سعر لكل المعدات
        return self.priceOfEquipment() + self.priceOfBigTools() + self.priceOfSmallTools()
    def totalOfCarpentryWoodsPerMeter(self): # سعر الخشب لكل متر
        return self.totalOfCarpentryWoods() / self.ceilingObj.sizeInMeterQuebed
    def totalOfCarpentryEquipmentAndToolsPerMeter(self): # سعر المعدات لكل متر
        return self.totalOfCarpentryEquipmentAndTools() / self.ceilingObj.sizeInMeterQuebed


