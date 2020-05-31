from .ai import AI


class Player:

    """
    This class defines the different players of the game (whether AI or
    real human being), and operates some methods on them.
    """

    def __init__(self, game, player_number):
        self.player_number = player_number  # 1 is purple 2 is blue
        self.game = game
        self.player_brain = None  # "ai" \ "boy"
        self.ai_brain = None  # object of ai

    def get_current_player_brain(self):
        """
        Description: This method get us the current player brain.
        :return: str
        """
        return self.player_brain

    def get_current_player_num(self):
        """
        Description: This method get us the current player.
        :return: int
        """
        return self.player_number

    def set_player_brain(self, brain_string):
        """
        Description: This method updates the current player attribute.
        :param brain_string: int
        :return: None
        """
        if brain_string == "ai":
            self.ai_brain = AI(self.game, self.player_number)
        else:
            self.ai_brain = None
        self.player_brain = brain_string

    def get_ai_brain(self):
        """
        Description: This method returns the ai object.
        :return: obj
        """
        return self.ai_brain
