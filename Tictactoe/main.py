import math
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player = "X"
print(board[0])
print(board[1])
print(board[2])
game_over = False
while game_over == False :
  while True:
    player_input = input("where do you want to place your peice.")
    if player_input .isnumeric():
      player_input = int(player_input)
      if player_input >= 1 and player_input <= 9:
        row = math.floor(player_input/3.0000001)
        column = ((player_input-1)%3)
        if board[row][column] == " ":
          board[row][column] = player
          print(board[0])
          print(board[1])
          print(board[2])
          if board[0][0] == board[0][1] == board[0][2] == player:
            print(board[0][0], "won")
            game_over = True
          elif board[1][0] == board[1][1] == board[1][2] == player:
            print(board[1][0], "won")
            game_over = True
          elif board[2][0] == board[2][1] == board[2][2] == player:
            print(board[2][0], "won")
            game_over = True
          elif board[0][0] == board[1][0] == board[2][0] == player:
            print(board[0][0], "won")
            game_over = True
          elif board[0][1] == board[1][1] == board[2][1] == player:
            print(board[0][1], "won")
            game_over = True
          elif board[0][2] == board[1][2] == board[2][2] == player:
            print(board[0][2], "won")
            game_over = True
          elif board[0][0] == board[1][1] == board[2][2] == player:
            print(board[0][0], "won")
            game_over = True
          elif board[0][2] == board[1][1] == board[2][0] == player:
            print(board[0][2], "won")
            game_over = True
            
          if player == "X":
            player = "O"
          else: 
            player = "X"
          
          break


"""board = [[" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " ", " "]]"""