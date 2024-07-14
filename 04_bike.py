# 04 Abstraction example

class Bike:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__mileage = 0

    def ride(self, distance):
        self.__mileage += distance
    
    def get_mileage(self):
        return self.__mileage
    
my_bike = Bike("Yamaha", "MT-07")
my_bike.ride(100)
print(my_bike.get_mileage())