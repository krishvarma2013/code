import random

def printboard():
  print (board[0])
  print (board[1])
  print (board[2])
  print (board[3])
  print (board[4])
  print (board[5])
piece = random.choice(["X", "O"])
gameover = False
board = [[" " for x in range(7)] for y in range(8)] 
printboard() 
while gameover is False:
  if piece == "O":
    player_input = input("Which coulumn do you want to place it in? ")
    player_input = int(player_input)
    print(player_input)
    for i in range(5, -1, -1):
      if board[i][player_input] == " ":
        board[i][player_input] = piece

        break
    
      
  elif piece == "X":
    piece_placed = False
    while piece_placed == False:
      piece_placed = False
      col = random.randint(0,6)
      for i in range(5, -1, -1):
            print(board[i][col])
            if board[i][col] == " ":
              board[i][col] = piece
              piece_placed = True
              break

      
  for i in range(0, 7):
    for j in range(5, 2, -1):
      if board[j][i] == piece and board[j+-1][i] == piece and board[j+-2][i] == piece and board[j+-3][i] == piece:
        print("Player", piece, "won")
        gameover = True

  for row in range(6):
    for column in range(0, 4):
      if board[row][column] == piece and board[row][column+1] == piece and board[row][column+2] == piece and board[row][column+3] == piece:
        print("Player", piece, "won")
        gameover = True


  positions = [[3, 0], [4, 0], [5,0], [3, 1], [4, 1], [5,1], [3, 2], [4, 2], [5,2], [3, 3], [4, 3], [5,3]]


  for pos in positions:
        if board[pos[0]][pos[1]] == piece and board[pos[0]-1][pos[1]+1] == piece and board[pos[0]-2][pos[1]+2] == piece and board[pos[0]-3][pos[1]+3] == piece:
          print("Player", piece, "won")
          gameover = True

  positions = [[5, 6], [4, 6], [3, 6], [5, 5], [4, 5], [3,5], [5, 4], [4, 4], [3,4], [5, 3], [4, 3], [3,3]]


  for pos in positions:
        if board[pos[0]][pos[1]] == piece and board[pos[0]-1][pos[1]-1] == piece and board[pos[0]-2][pos[1]-2] == piece and board[pos[0]-3][pos[1]-3] == piece:
          print("Player", piece, "won")
          gameover = True
  if piece == "O":
    piece = "X"
  else: 
    piece = "O"
  printboard()
