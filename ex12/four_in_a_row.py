import tkinter as tki
from ex12.ai import *
from ex12.players import Player
from ex12.gui import Gui
from ex12.game import *

class MainGame:

    """
    This class is the main class which operates the game itself.
    This class calls the game, and the gui classes to action.
    """

    def __init__(self):
        """resets the initial game details"""
        self.root = tki.Tk()
        self.root.title("it's adi and orel bat mitzva!!!")
        self.game = Game()
        # creates all players instances
        self.player1 = Player(self.game, 1)  # purple
        self.player2 = Player(self.game, 2)  # blue

    def gui_go(self):
        """
        Description: This method starts the Gui visualization.
        :return: None
        """
        # start the gui of the game!
        self.gui = Gui(self, self.root, self.game, self.player1, self.player2)
        self.gui.root.mainloop()

    def restart_game(self):
        """
        Description: This method starts the game and defines the two
        players of the game.
        :return: None
        """
        self.game = Game()
        # create all players instances
        self.player1 = Player(self.game, 1)  # purple
        self.player2 = Player(self.game, 2)  # blue


if __name__ == '__main__':
    main_game = MainGame()
    main_game.gui_go()
