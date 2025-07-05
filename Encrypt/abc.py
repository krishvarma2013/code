def encode(shifts , message):
  alphabet = ("abcdefghijklmnopqrstuvwxyz")
  tebahpla = ("")
  for character in message:
    if character in alphabet:
      newindex = (alphabet.index(character) + shifts) % 26
      tebahpla += alphabet[newindex]
    else:
      print ("Error")
  return tebahpla
  
def decode(shifts, message):
  alphabet = ("abcdefghijklmnopqrstuvwxyz")
  tebahpla = ("")
  for character in message:
    if character in alphabet:
      newindex = (alphabet.index(character) - shifts) % 26
      tebahpla += alphabet[newindex]
    else:
      print ("Error")
  return tebahpla

playerrr_input = input("Do you want to encode or decode?")
player_input = input("What's your message?")
playerr_input = input("How much shifts do you want?")
if playerrr_input == encode:
  print (encode(playerr_input, player_input))
if playerrr_input == decode:
  print (decode(playerr_input, player_input))

 


