import random
from colorama import Fore, Style


def horse_betting():
  money = random.randint(0, 50000)
  print("You Have : ", money, "$")
  bet = 0
  gameend = False
  while gameend == False:
    amt_bet = int(input("Enter Bet amount : "))
    if amt_bet > money:
      print(
          "Too Big Bet! System automatically set the bet as your entire balance."
      )
      amt_bet = money
    menu = int(
        input(
            "This is a horse racing event. Type 1 to bet on Horse 1, Type 2 to bet on Horse 2, Type 3 to bet on Horse 3, Type 4 to bet on Horse 4, Type 5 to bet on Horse 5, Type 6 to bet on Horse 6, Type 7 to bet on Horse 7, Type 8 to bet on Horse 8, Type 9 to bet on Horse 9, and Type 10 to bet on Horse 10."
        ))
    bet += amt_bet
    ran = random.randint(1, 10)
    if ran == 1:
      print("Horse 1 has won")
    elif ran == 2:
      print("Horse 2 has won")
    elif ran == 3:
      print("Horse 3 has won")
    elif ran == 4:
      print("Horse 4 has won")
    elif ran == 5:
      print("Horse 5 has won")
    elif ran == 6:
      print("Horse 6 has won")
    elif ran == 7:
      print("Horse 7 has won")
    elif ran == 8:
      print("Horse 8 has won")
    elif ran == 9:
      print("Horse 9 has won")
    elif ran == 10:
      print("Horse 10 has won")

    if menu != ran:
      print("Womp Womp You lost.")
      print("You now have ", money - amt_bet, "$")
      money -= amt_bet
    if menu == ran:
      print("You won!")
      print("You now have ", amt_bet * 1.6 + (money + amt_bet), "$")
      money += amt_bet * 1.6
    a = int(input("Press 1 to end game, or Press 2 to bet more."))
    if a == 1:
      gameend = True
    if a == 2:
      gameend = False

  if gameend == True:
    print("Bet Amount : ", bet, "$")
    print("Earn Amount : ", money, "$")

def question():
  game_ask_list = []
  game_ask = input("Would you like to play a game? ")
  if game_ask.lower() == "no":
    print("Why are u here then 😑")
  elif game_ask.lower() == "yes":
    horse_betting()








question()
'''while 'yes'in game_ask_list:
game_ask = input("One more time? ")
game_ask_list = []
for x in game_ask:
  game_ask_list.append(x.lower())'''

