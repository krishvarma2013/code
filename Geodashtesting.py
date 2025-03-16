


from os import X_OK
from typing import Text


'''board = [["......................................................"], 
  ["......................................................"], 
  ["......................................................"], 
  ["......................................................"], 
  ["......................................................"], 
  ["......................................................"], 
  ["......................................................"], 
  ["......................................................"], 
  ["......................................................"], 
  ["......................................................"], 
  ["......................................................"], 
  [".................................^^^^................."], 
  ["..........^^^.............XXXXXXXXXXXXXXXXXXXXXXXXXXXX"], 
  ["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"], 
  ["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"], 
  ["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]]


print(board[0])
print(board[1])
print(board[2])
print(board[3])
print(board[4])
print(board[5])
print(board[6])
print(board[7])
print(board[8])
print(board[9])
print(board[10])
print(board[11])
print(board[12])
print(board[13])
print(board[14])
print(board[15])'''

y = 0
for list in board:
  x = 0
  y += 1
  print ("")
  for tile in list:
    print (tile, end = "")
    x += 1


print("READ FILE MAP")

file = open("nnn.txt", "r")
txt = file.readlines()
y = 0
for lines in txt:
  x = 0
  y += 1
  print ("")
  for tile in lines:
    print (tile, end = "")
    x += 1
