class Game:

    """
    This class defines the game and its attributes (visual board,
    coordinates of the board and the current player of the game), in addition
    this class operates some method on the game object.
    """

    def __init__(self):
        self.__visual_board = [["_" for a in range(7)] for b in range(6)]
        self.__coordinates_board = [(a, b) for a in range(6) for b in
                                    range(7)]
        self.__current_player = 1
        self.__first_convert_dict = {(3, 0): (3, 0), (4, 0): (4, 0),
                                     (4, 1): (3, 1), (5, 0): (5, 0),
                                     (5, 1): (4, 1), (5, 2): (3, 2),
                                     (6, 0): (5, 1), (6, 1): (4, 2),
                                     (6, 2): (3, 3)}
        self.__second_convert_dict = {(3, 0): (2, 0), (4, 0): (1, 0),
                                      (4, 1): (2, 1), (5, 0): (0, 0),
                                      (5, 1): (1, 1), (5, 2): (2, 2),
                                      (6, 0): (0, 1), (6, 1): (1, 2),
                                      (6, 2): (2, 3), (7, 0): (0, 2),
                                      (7, 1): (1, 3), (8, 0): (0, 3)}

    def get_first_convert_dict(self):
        """
        Description: This method returns the dictionary which
        contains connect between coordinates of the convert board with the
        coordinates of the original game board.
        :return: dict
        """
        return self.__first_convert_dict

    def get_second_convert_dict(self):
        """
        Description: This method returns the dictionary which
        contains connect between coordinates of the convert board with the
        coordinates of the original game board.
        :return: dict
        """
        return self.__second_convert_dict

    def get_current_player(self):
        """
        Description: This method get us the current player.
        :return: int
        """
        return self.__current_player

    def set_current_player(self, player_num):
        """
        Description: This method updates the current player attribute.
        :param player_num: int
        :return: None
        """
        self.__current_player = player_num

    def get_visual_board(self):
        """
        Description: This method get us the visual board.
        :return: list
        """
        return self.__visual_board

    def set_visual_board(self, row, column, string):
        """
        Description: This method updates the visual board.
        :param row: int
        :param column: int
        :param string: str
        :return: None
        """
        self.__visual_board[row][column] = string

    def get_coordinates_board(self):
        """
        Description: This method get us the list of the board of coordinates.
        :return: list
        """
        return self.__coordinates_board

    def make_move(self, column):
        """
        Description: This method changes the disc board if the given column
        is legal (empty and defined in the board).
        :param column: int
        :return: None
        """
        player = str(self.get_current_player())
        coor_list = self.get_coordinates_board()
        current_board = self.get_visual_board()
        for row in range(5, -1, -1):

            if (row, column) in coor_list:
                if current_board[row][column] == "_":
                    self.set_visual_board(row, column, player)
                    # updates the player number
                    self.define_player(player)
                    return row
            # If the coordinates is not legal (is not in the board)
            else:
                raise Exception("Illegal move.")
        # If the column is not empty
        raise Exception("Illegal move.")

    def find_win_coordinates(self):
        """
        Description: This method check which is the first coordinates and
        the last coordinates of a winning sequence in the game.
        :return: list
        """
        coor_list = []
        first_board = self.get_visual_board()
        if self.find_coordinates(first_board):
            # checks rows
            row, col = self.find_coordinates(first_board)
            coor_list.append((row, col))
            coor_list.append((row, col + 3))

        second_board = self.check_columns(first_board)
        if self.find_coordinates(second_board):
            # checks columns (from up to down)
            col, row = self.find_coordinates(second_board)
            coor_list.append((row, col))
            coor_list.append((row + 3, col))

        third_board = self.check_diagonals_up_and_right(first_board)
        if self.find_coordinates(third_board):
            # checks diagonals from left and down to up and right
            row, col = self.find_coordinates(third_board)
            first_dict = self.get_first_convert_dict()
            if (row, col) in first_dict:
                new_row, new_col = first_dict.get((row, col))
                coor_list.append((new_row, new_col))
                coor_list.append((new_row - 3, new_col + 3))

        fourth_board = self.check_diagonals_down_and_right(first_board)
        if self.find_coordinates(fourth_board):
            # checks diagonals from left and up to down and right
            row, col = self.find_coordinates(fourth_board)
            second_dict = self.get_second_convert_dict()
            if (row, col) in second_dict:
                new_row, new_col = second_dict.get((row, col))
                coor_list.append((new_row, new_col))
                coor_list.append((new_row + 3, new_col + 3))

        return coor_list

    def find_coordinates(self, board):
        """
        Description: This method returns the first winning coordinates of
        the convert board.
        :param board: list
        :return: tuple
        """
        for row in range(len(board)):
            cur_row = "".join(board[row])
            if "1111" in cur_row:
                column = cur_row.index("1111")
                return row, column
            elif "2222" in cur_row:
                column = cur_row.index("2222")
                return row, column
        # If there is no sequence
        return False

    def define_player(self, player):
        """
        Description: This method changes the current player'to the other
        player.
        :param player: str
        :return: None
        """
        players_list = ["1", "2"]
        players_list.pop(players_list.index(player))
        self.set_current_player(int(players_list[0]))

    def get_winner(self):
        """
        Description: This method checks if someone won in the game, or the
        board is full and there is a tie.
        :return: int - if the game ended, None - if the game did not end.
        """
        first_board = self.get_visual_board()
        if self.check_rows(first_board):
            return self.check_rows(first_board)  # If there is a winner

        second_board = self.check_columns(first_board)
        if self.check_rows(second_board):
            return self.check_rows(second_board)  # If there is a winner

        third_board = self.check_diagonals_up_and_right(first_board)
        if self.check_rows(third_board):
            return self.check_rows(third_board)  # If there is a winner

        fourth_board = self.check_diagonals_down_and_right(first_board)
        if self.check_rows(fourth_board):
            return self.check_rows(fourth_board)  # If there is a winner

        # If there is no winner, checks if the board is full
        coor_list = self.get_coordinates_board()
        current_board = self.get_visual_board()
        for coordinate in coor_list:
            if current_board[coordinate[0]][coordinate[1]] == "_":
                return None  # If the board is not full

        return 0  # If the board is full and their is a tie

    def check_columns(self, board):
        """
        Description: This method converts the board's columns to list of
        lists.
        :param board: list
        :return: list
        """
        new_board = []
        for column in range(7):
            new_list = []
            for row in range(6):
                new_list.append(board[row][column])
            new_board.append(new_list)

        return new_board

    def check_diagonals_up_and_right(self, board):
        """
        Description: This method converts the board's diagonals (up and
        right) to list of lists.
        :param board: list
        :return: list
        """
        column_num = 7
        row_num = 6
        lists_num = column_num + row_num - 1
        new_board = []

        # this part creates lists inside one huge list
        for list_num in range(lists_num):
            new_board.append([])

        # this part enters letters inside the relevant list
        for column in range(column_num):
            for row in range(row_num):
                num_list_matrix = column + row
                matrix_coordinate = board[row][column]
                new_board[num_list_matrix].append(matrix_coordinate)

        return new_board

    def check_diagonals_down_and_right(self, board):
        """
        Description: This method converts the board's diagonals (down and
        right) to list of lists.
        :param board: list
        :return: list
        """
        column_num = 7
        row_num = 6
        lists_num = column_num + row_num - 1
        new_board = []

        # this part creates lists inside one huge list
        for list_num in range(lists_num):
            new_board.append([])

        subtrahend = 1 - row_num

        # this part enters letters inside the relevant list
        for column in range(column_num):
            for row in range(row_num):
                num_list_matrix = column - (row + subtrahend)
                matrix_coordinate = board[row][column]
                new_board[num_list_matrix].append(matrix_coordinate)

        return new_board

    def check_rows(self, board):
        """
        Description: This method checks if there is a sequence of 4 '1' or
        '2' in the list.
        :param board: list
        :return: int - if there is a winner, False - otherwise
        """
        for row in range(len(board)):
            cur_row = "".join(board[row])
            if "1111" in cur_row:
                return 1
            elif "2222" in cur_row:
                return 2
        # If there is no sequence
        return False

    def get_player_at(self, row, col):
        """
        Description: This method gets a location, checks if the location is
        legal, if it is, it returns the disc in this place.
        :param row: int
        :param col: int
        :return: None - if the location is empty or illegal, or srt if it
        is not empty.
        """
        if (row, col) in self.get_coordinates_board():
            cur_box = self.get_visual_board()[row][col]
            if cur_box == "_":
                return None
            else:
                return cur_box
        else:
            raise Exception("Illegal location.")
