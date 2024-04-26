import numpy as np


class TicTacToe:
    def __init__(self):
        game_board_content = [['1', '2', '3'],
                              ['4', '5', '6'],
                              ['7', '8', '9']]
        self.signs = ["X", "O"]
        self.game_board_content = np.asarray(game_board_content)
        self.board_display = ""
        self.update_board()
        self.current_player = 1
        self.current_sign = "X"

    def set_player(self):
        if self.current_player == 1:
            self.current_player = 2
            self.current_sign = "O"
        else:
            self.current_player = 1
            self.current_sign = "X"

    def update_board(self):
        self.board_display = f"""
         {self.game_board_content[0][0]} | {self.game_board_content[0][1]} | {self.game_board_content[0][2]} 
        ------------
         {self.game_board_content[1][0]} | {self.game_board_content[1][1]} | {self.game_board_content[1][2]} 
        ------------
         {self.game_board_content[2][0]} | {self.game_board_content[2][1]} | {self.game_board_content[2][2]} 
        """

    def display_board(self):
        self.update_board()
        print(self.board_display)

    def display_player(self):
        if self.current_sign == "X":
            print("Player 1 move.")
        elif self.current_sign == "O":
            print("Player 2 move.")
        else:
            raise Exception("Unknown sign was given!")

    def display_result(self, result):
        if result == 0:
            print("DRAW !")
        elif result == 1:
            print(f"Player number {self.current_player} WINS !")
        else:
            raise Exception("Unknown type of game ending!")

    def mark(self):
        position = input(f"Select available position to mark {self.current_sign}: ")
        if not position.isdigit():
            print("You entered not a number character!")
            return False
        if any(position in x for x in self.game_board_content):
            coordinates = list(zip(*np.where(self.game_board_content == position)))
            self.game_board_content[coordinates[0][0]][coordinates[0][1]] = self.current_sign
            return True
        else:
            print("You entered unavailable position!")
            return False

    def check_win(self):

        # check if there are 3 the same signs in any row
        for i, row in enumerate(self.game_board_content):
            if all(x == self.current_sign for x in row):
                return True

        # check if there are 3 the same signs in any column
        for i in range(len(self.game_board_content[0])):
            if all(x == self.current_sign for x in self.game_board_content[:, i]):
                return True

        # check if there are 3 the same signs in first diagonal
        first_diagonal = []
        for i, row in enumerate(self.game_board_content):
            first_diagonal.append(row[i])
        if all(x == self.current_sign for x in first_diagonal):
            return True

        # check if there are 3 the same signs in second diagonal
        second_diagonal = []
        for i, row in enumerate(self.game_board_content[::-1]):
            second_diagonal.append(row[i])
        if all(x == self.current_sign for x in second_diagonal):
            return True

        return False

    def check_draw(self):
        for row in self.game_board_content:
            for value in row:
                if value not in self.signs:
                    return False
        return True


