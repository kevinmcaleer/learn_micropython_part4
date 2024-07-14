# 13 Getter and Setter

class Robot:
    def __init__(self, name):
        self.name = name
        self.__speed = 0

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            self.__speed = 0
        elif value > 100:
            self.__speed = 100
        else:
            self.__speed = value

r = Robot("Robbie")
r.speed = 50
print(r.speed)  
r.speed = 150
print(r.speed)  # notice the speed was capped at 100