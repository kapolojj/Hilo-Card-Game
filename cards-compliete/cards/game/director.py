import os
os.system("cls")
import random
from game.die import Die


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        dice (List[Die]): A list of Die instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """
    

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 300
        
        



    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        self.random_value1 = random.randint(1, 13)
        print(f"The card is: {self.random_value1}")

        self.card = input("Higher or Lower? [h/l] ")
        self.random_value2 = random.randint(1, 13)
        print(f"The card is: {self.random_value2}")
       
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        if self.random_value1 < self.random_value2 and self.card == "h":
            self.score += 100
        elif self.random_value1 > self.random_value2 and self.card == "l":
            self.score += 100
        else:
            self.score -= 75


    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Your score is equal to: {self.score}")
        self.play_again = input("Play again? [y/n] ")
        if self.play_again == "y":
            self.is_playing == (self.score > 0)
        else:
            print(f"Thank you for playing")
