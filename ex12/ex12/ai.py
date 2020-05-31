import random


class AI:

    """
    This class defines the legal column the ai player can choose in order
    to put disc in this column of the board game.
    """

    def __init__(self, game, player):
        self.__game = game
        self.__player = player

    def find_legal_move(self, timeout=None):
        """
        Description: This method randoms a legal value for the column
        :param timeout: None
        :return: int
        """
        current_game = self.get_game()
        game_status = str(current_game.get_winner())
        if game_status == "0" or game_status == "1" or game_status == "2":
            # If the game ended - someone won / the board is full
            raise Exception("No possible AI moves")

        legal_column_lst = []
        for column in range(7):
            for row in range(0, 6):
                # We start to check the highest rows (because the bigger
                # probability of them to be empty)

                if current_game.get_player_at(row, column) == None:
                    # If this coordination is empty
                    legal_column_lst.append(column)
                break  # Checks the followed column

        # Randoms a legal value for column
        random_column = random.choice(legal_column_lst)
        return random_column

    def get_game(self):
        """
        Description: This method returns the game object.
        :return: obj
        """
        return self.__game

    def get_last_found_move(self):
        pass
