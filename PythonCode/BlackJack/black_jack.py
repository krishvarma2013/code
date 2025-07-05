import random
import sys

money = random.randint(0, 50000)
print("You Have : ", money, "$")
bet = 0
gameover = False
a=""

amt_bet = int(input("Enter Bet amount : "))
if amt_bet > money:
  print(
      "Too Big Bet! System automatically set the bet as your entire balance."
  )
  amt_bet = money
bet += amt_bet
print (amt_bet)
  

cards = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
def draw(hand):
  card = random.choice(cards)
  print (card)
  hand.append(card)
  return hand
def dra(hand):
  card = random.choice(cards)
  hand.append(card)
  print ("#")
  return hand
playerhand = []
dealerhand = []
def gettotal(hand):
  total = 0
  for card in hand:
    if card in ["Ace"]:
      total += 11
    elif card in ["King", "Queen", "Jack"]:
      total += 10
    else:
      total += int(card)
  return total


def betting(): 
  global money, bet, gameover, amt_bet,a
  

  print("your hand:")
  draw(playerhand)
  draw(playerhand)
  print("total = ", gettotal(playerhand))
  print("dealer hand:")
  draw(dealerhand)
  dra(dealerhand)
  playerinput = ""
  while True:
    if gettotal(playerhand) == 21:
      gameover = True
      break
    elif gettotal(playerhand) > 21:
      print ("You lose")
      a = int(input("Press 1 to end game, or Press 2 to bet more."))

      
    playerinput = input("Do you want to draw or quit your turn? ")
    if playerinput == "draw":
      draw(playerhand)
      print(playerhand)
      print(gettotal(playerhand))
      
    if playerinput == "quit":
      break
  while True and gameover == False:
    dealerchoice = ["quit", "draw"]
    dealerchoice = random.choice(dealerchoice)
    if dealerchoice == "draw":
      print ("dealer did draw")
      print(dealerhand)
      draw(dealerhand)
      print(gettotal(dealerhand))
      if gettotal(dealerhand) > 20:
        break
    if dealerchoice == "quit":
      print ("dealer didnt draw")
      a = int(input("Press 1 to end game, or Press 2 to bet more."))

  
  
    
  
  
  print("player total:", gettotal(playerhand))
  print("dealer total:", gettotal(dealerhand))
  
  
  
  if gettotal(playerhand) > 21:
    print("You lost")
    print("You now have ", money - amt_bet, "$")
    money -= amt_bet
    a = int(input("Press 1 to end game, or Press 2 to bet more."))

  elif gettotal(dealerhand) > 21:
    print("You now have ", amt_bet * .6 + (money + amt_bet), "$")
    money += amt_bet * .6
    print("You won")
    a = int(input("Press 1 to end game, or Press 2 to bet more."))

  elif gettotal(playerhand) == 21:
    print("You now have ", amt_bet * .6 + (money + amt_bet), "$")
    money += amt_bet * .6
    print("You won")
    a = int(input("Press 1 to end game, or Press 2 to bet more."))

  elif gettotal(dealerhand) == 21:
    print("You lost")
    print("You now have ", money - amt_bet, "$")
    money -= amt_bet
    a = int(input("Press 1 to end game, or Press 2 to bet more."))

  elif gettotal(playerhand)>gettotal(dealerhand):
    print("You win")
    print("You now have ", amt_bet * .6 + (money + amt_bet), "$")
    money += amt_bet * .6
    a = int(input("Press 1 to end game, or Press 2 to bet more."))

  elif gettotal(dealerhand)>gettotal(playerhand):
    print("You lose")
    print("You now have ", money - amt_bet, "$")
    money -= amt_bet
    a = int(input("Press 1 to end game, or Press 2 to bet more."))
  
  if a == 1:
    gameover = True
    sys.exit()
  if a == 2:
    gameover = False
    betting()
 
  
  if gameover == True:
    print("Bet Amount : ", bet, "$")
    print("Earn Amount : ", money, "$")

betting()










































































  

'''import random
monkey = ["drippycheese", "friesbag", "moldycheese"]
monkey = random.choice(monkey)
player_input = input("what do you want to use: drippycheese (rock), friesbag (scissors), or moldycheese (paper) " )

if monkey == "drippycheese" and player_input == "friesbag":
  print ("monkey won")
if monkey == "friesbag" and player_input == "moldycheese":
  print ("monkey won")
if monkey == "moldycheese" and player_input == "drippycheese":
  print ("monkey won")
if player_input == "drippycheese" and monkey == "friesbag":
  print ("you won")
if player_input == "friesbag" and monkey == "moldycheese":
  print ("you won")
if player_input == "moldycheese" and monkey == "drippycheese":
  print ("you won")
if monkey == player_input:
  print ("tie")'''




