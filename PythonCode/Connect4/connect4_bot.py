import random

NUM_ROWS = 6
NUM_COLS = 7
EMPTY_SLOT = " "
CONNECT_FOUR = 4

def print_game_board():
    print("  " + " ".join(str(i) for i in range(NUM_COLS)))
    for r in range(NUM_ROWS):
        print(f"{r} |" + "|".join(game_board[r][c] for c in range(NUM_COLS)) + "|")
    print("  " + "-" * (NUM_COLS * 2 + 1))

def check_for_win(board_state, current_piece):
    for r_check in range(NUM_ROWS):
        for c_check in range(NUM_COLS - CONNECT_FOUR + 1):
            if all(board_state[r_check][c_check + i] == current_piece for i in range(CONNECT_FOUR)):
                return True

    for c_check in range(NUM_COLS):
        for r_check in range(NUM_ROWS - CONNECT_FOUR + 1):
            if all(board_state[r_check + i][c_check] == current_piece for i in range(CONNECT_FOUR)):
                return True

    for r_check in range(NUM_ROWS - CONNECT_FOUR + 1):
        for c_check in range(NUM_COLS - CONNECT_FOUR + 1):
            if all(board_state[r_check + i][c_check + i] == current_piece for i in range(CONNECT_FOUR)):
                return True

    for r_check in range(NUM_ROWS - CONNECT_FOUR + 1):
        for c_check in range(CONNECT_FOUR - 1, NUM_COLS):
            if all(board_state[r_check + i][c_check - i] == current_piece for i in range(CONNECT_FOUR)):
                return True

    return False

current_player_piece = random.choice(["X", "O"])
game_is_over = False
game_board = [[EMPTY_SLOT for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

print_game_board()

while not game_is_over:
    selected_column = -1

    if current_player_piece == "O":
        while True:
            try:
                column_input_str = input(f"Player {current_player_piece}, enter column (0-{NUM_COLS-1}) to drop your piece: ")
                player_chosen_column = int(column_input_str)

                if 0 <= player_chosen_column < NUM_COLS:
                    if game_board[0][player_chosen_column] == EMPTY_SLOT:
                        for row_to_drop in range(NUM_ROWS - 1, -1, -1):
                            if game_board[row_to_drop][player_chosen_column] == EMPTY_SLOT:
                                game_board[row_to_drop][player_chosen_column] = current_player_piece
                                selected_column = player_chosen_column
                                break
                        break
                    else:
                        print("That column is full. Please choose a different one.")
                else:
                    print(f"Invalid column number. Please enter a number between 0 and {NUM_COLS-1}.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    elif current_player_piece == "X":
        print(f"Player {current_player_piece} The bot is making a move...")
        while True:
            ai_chosen_column = random.randint(0, NUM_COLS - 1)
            
            if game_board[0][ai_chosen_column] == EMPTY_SLOT:
                for row_to_drop in range(NUM_ROWS - 1, -1, -1):
                    if game_board[row_to_drop][ai_chosen_column] == EMPTY_SLOT:
                        game_board[row_to_drop][ai_chosen_column] = current_player_piece
                        selected_column = ai_chosen_column
                        print(f"The bot dropped piece in column {ai_chosen_column}.")
                        break
                break

    print_game_board()

    if check_for_win(game_board, current_player_piece):
        print(f"Player {current_player_piece} wins! 🎉 Congratulations!")
        game_is_over = True
    else:
        board_is_full = True
        for col_index in range(NUM_COLS):
            if game_board[0][col_index] == EMPTY_SLOT:
                board_is_full = False
                break
        
        if board_is_full:
            print("The board is full! It's a draw. 🤝")
            game_is_over = True
    
    if not game_is_over:
        if current_player_piece == "O":
            current_player_piece = "X"
        else:
            current_player_piece = "O"