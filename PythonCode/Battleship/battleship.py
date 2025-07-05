def printboard(board_to_print):
  print(board_to_print[0])
  print(board_to_print[1])
  print(board_to_print[2])
  print(board_to_print[3])
  print(board_to_print[4])
  print(board_to_print[5])
  print(board_to_print[6])
  print(board_to_print[7])
  print(board_to_print[8])
  print(board_to_print[9])


shipnumber = 0
gameover = False 
board = [[" " for x in range(10)] for y in range(10)]
printboard(board) 
boardshooting = [[" " for x in range(10)] for y in range(10)]
board2 = [[" " for x in range(10)] for y in range(10)]
boardshooting2 = [[" " for x in range(10)] for y in range(10)]
ships = [5, 4, 3, 3, 2]
score = 0
score2 = 0
while shipnumber < 5:
  rowinput = int(input("What row do you want to place the piece on? "))
  colinput = int(input("What column do you want to place the piece on? "))
  print(rowinput, colinput)
  dirinput = input(
      "What direction do you want to place the piece on: H or V? ")

  if dirinput not in ["H", "h", "V", "v"] or colinput not in range(10)  or rowinput not in range(10):
    print ("try again")
  
  elif dirinput in ["h", "H"]:
    if colinput + ships[shipnumber] < 10:
      for i in range(ships[shipnumber]):
        if board[rowinput][colinput + i] == " ":
          if i == ships[shipnumber] - 1:
            for i in range(ships[shipnumber]):
              board[rowinput][colinput + i] = "X"
            shipnumber += 1
        else:
          print("invalid position try again")
          break

  elif dirinput in ["v", "V"]:
    if rowinput + ships[shipnumber] < 10:
      for i in range(ships[shipnumber]):
        if board[rowinput + i][colinput] == " ":
          if i == ships[shipnumber] - 1:
            for i in range(ships[shipnumber]):
              board[rowinput + i][colinput] = "X"
            shipnumber += 1
        else:
          print("invalid position try again")
          break


  printboard(board)

# PLAYER 2
shipnumber = 0
print("### Player 2 ###")
while shipnumber < 5:
  rowinput = int(input("What row do you want to place the piece on? "))
  colinput = int(input("What column do you want to place the piece on? "))
  print(rowinput, colinput)
  dirinput = input(
      "What direction do you want to place the piece on: H or V? ")

  if dirinput not in ["H", "h", "V", "v"] or colinput not in range(10)  or rowinput not in range(10):
    print ("try again")

  elif dirinput in ["h", "H"]:
    if colinput + ships[shipnumber] < 10:
      for i in range(ships[shipnumber]):
        if board2[rowinput][colinput + i] == " ":
          if i == ships[shipnumber] - 1:
            for i in range(ships[shipnumber]):
              board2[rowinput][colinput + i] = "X"
            shipnumber += 1
        else:
          print("invalid position try again")
          break

  elif dirinput in ["v", "V"]:
    if rowinput + ships[shipnumber] < 10:
      for i in range(ships[shipnumber]):
        if board2[rowinput + i][colinput] == " ":
          if i == ships[shipnumber] - 1:
            for i in range(ships[shipnumber]):
              board2[rowinput + i][colinput] = "X"
            shipnumber += 1
        else:
          print("invalid position try again")
          break
  printboard(board2)

# SHOOTING
currentTurn = 1
while gameover == False:
  if currentTurn == 1:
    print("Player 1")
    try:
      rowinput = int(input("What row do you want to shoot? "))
      colinput = int(input("What column do you want to shoot? "))
    except Exception:
      print("Invalid input. Try again.")
      continue
    if rowinput not in range(10) or colinput not in range(10):
      print("Invalid input. Try again.")
      continue
    print(rowinput, colinput)
    if board2[rowinput][colinput] == "X":
      print("Hit")
      score += 1
      print(score)
      boardshooting2[rowinput][colinput] = "X"
      if currentTurn == 1:
        currentTurn = 2
      else: 
        currentTurn = 1
    if board2[rowinput][colinput] == " ":
      print("No hit")
      boardshooting2[rowinput][colinput] = "O"
      if currentTurn == 1:
        currentTurn = 2
      else: 
        currentTurn = 1
    printboard(boardshooting2)
  if currentTurn == 2:
    print("Player 2")
    try:
      rowinput = int(input("What row do you want to shoot? "))
      colinput = int(input("What column do you want to shoot? "))
    except Exception:
      print("Invalid input. Try again.")
      continue
    if rowinput not in range(10) or colinput not in range(10):
      print("Invalid input. Try again.")
      continue
    print(rowinput, colinput)
    if board[rowinput][colinput] == "X":
      print("Hit")
      score2 += 1
      print(score2)
      if currentTurn == 1:
        currentTurn = 2
      else: 
        currentTurn = 1
      boardshooting[rowinput][colinput] = "X"
    if board[rowinput][colinput] == " ":
      print("No hit")
      boardshooting[rowinput][colinput] = "O"
      if currentTurn == 1:
        currentTurn = 2
      else: 
        currentTurn = 1
    printboard(boardshooting)

  if score == 17:
    gameover = True
    print ("Player 1 Won")

  if score2 == 17:
    gameover = True
    print ("Player 2 Won")
  
                                
                            
      
    
      