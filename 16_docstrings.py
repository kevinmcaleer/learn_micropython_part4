# 16 DocStrings

class Robot:
    """
    A class to represent a robot.
    
    Attributes:
    name (str): The name of the robot.
    speed (int): The speed of the robot.
    
    Methods:
    greet():
        Greets the user.
    set_speed(speed):
        Sets the speed of the robot.
    """

    def __init__(self, name, speed=0):
        """
        Constructs all the necessary attributes for the robot object.

        Parameters:
        name (str): The name of the robot.
        speed (int): The speed of the robot.
        """
        self.name = name
        self.speed = speed

    def greet(self):
        """
        Greets the user by printing a greeting message.
        """
        print(f"Hello, I am {self.name}")

    def set_speed(self, speed):
        """
        Sets the speed of the robot.

        Parameters:
        speed (int): The new speed of the robot.
        """
        self.speed = speed

# Create a robot object

r = Robot("Robo") # Hover over the class name to see the docstring