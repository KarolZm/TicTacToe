from tic_tac_toe import TicTacToe


game_board = TicTacToe()
game_board.display_board()

while True:
    # Display active player
    game_board.display_player()

    # Select position until correct
    while not game_board.mark():
        pass

    # Display game board
    game_board.display_board()

    # Check if current player wins
    if game_board.check_win():
        game_board.display_result(1)
        break

    # Check if draw
    if game_board.check_draw():
        game_board.display_result(0)
        break

    # Change player
    game_board.set_player()
