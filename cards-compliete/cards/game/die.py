import random


class Die:
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
    """

    def __init__(self):
        """Constructs a new instance of Die.

        Args:
            self (Die): An instance of Die.
        """
        self.value = 0
        self.points = 300

    def roll(self):
        """Generates a new random value and calculates the points for the die.
        
        Args:
            self (Die): An instance of Die.
        """
        self.value = random.randint(1, 13)
        self.points = 100 if self.value == 5 else -75 if self.value == 75 else 0