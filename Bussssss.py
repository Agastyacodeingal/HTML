class vehicle:
    def __init__(self,name,mileage):
        self.name = name
        self.mileage = mileage
class bus (vehicle):
    def __init__(self, name, mileage,brand):
        vehicle. __init__(self,name,mileage)
        self.brand_n = brand
    def print_bus(self):
        print("The vehicle name is ",self.name)
        print("The vehicles brand is ",self.brand_n)
        print("The vehicles mileage is ",self.mileage)
b1 = bus("volv0","999999","BEST")
b1.print_bus()