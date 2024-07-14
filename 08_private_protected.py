# 07 Private and Protected Proproties

class Car():

    __fuel_type = "petrol" # Private property

    def __init__(self, fuel:str=None):
        # Sets the fuel type of the car
        if fuel is not None:
            self.__fuel_type = fuel

    def __str__(self):
        # Returns the fuel type of the car
        return f"Fuel type is {self.__fuel_type}"
    
    def __private_method(self):
        # This is a private method
        print("This is a private method")

    def _protected_method(self):
        # This is a protected method
        print("This is a protected method")
    
    def public_method(self):
        # This is a public method
        print("This is a public method")
    
gas_guzzler = Car()
zoe = Car(fuel="Electric")

# try and access the private property
zoe.public_method()
zoe._protected_method()
zoe.__private_method()

print(zoe)
print(gas_guzzler)