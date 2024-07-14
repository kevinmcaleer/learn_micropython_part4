# 05 Modularity

class Sensor:
    def __init__(self, type):
        self.type = type

    def read_value(self):
        # Simulate reading a sensor value
        return 42

class Motor:
    def __init__(self, power):
        self.power = power

    def move(self, direction):
        print(f"Moving {direction} with power {self.power}")

class Robot:
    def __init__(self, name):
        self.name = name
        self.sensor = Sensor("Ultrasonic")
        self.motor = Motor(100)

    def move_forward(self):
        self.motor.move("forward")

    def read_sensor(self):
        return self.sensor.read_value()

robot = Robot("Robo")
robot.move_forward()
print(robot.read_sensor())