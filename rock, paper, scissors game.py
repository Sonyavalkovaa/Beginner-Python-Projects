print("EPIC 🪨📄✂️ BATTLE")
print()
from getpass import getpass as input
print("Select your move (R, P, or S)")
print()
player1_score = 0
player2_score = 0

while True: 
  Player1move = input("player_1> ")
  print()
  Player2move = input("player_2> ")
  print()
  if Player1move == "R":
    if Player2move == "R":
      print("You both picked rock, take another turn!")
    elif Player2move == "P":
      print("Rock of player 1 has been wrapped around by paper of player 2!")
      player2_score += 1
    elif Player2move == "S":
      print("Haha, player 2 scissors! You have been broken by the rock of player 1!")
      player1_score += 1
    else: 
      print("Invalid move. Please take another turn.")
  elif Player1move == "P": 
    if Player2move == "S":
      print("Congrads! You have beaten up the paper of player 1!")
      player1_score += 1
    elif Player2move == "R": 
      print("Player 2's rock has been crushed by the paper of player 1!")
      player1_score += 1
    elif Player2move == "P": 
      print("Come on, this is very dissapointing. Draw again.")
    else: 
      print("Invalid move. Please try again.")
  elif Player1move == "S": 
    if Player2move == "S": 
      print("Two scissors are having an endless fight. Let's dissolve this now.")
    elif Player2move == "R": 
      print("Player 1, lie in peace! You have been corrupted by the scissors of player 2!")
      player2_score += 1
    elif Player2move == "P": 
      print("player 2's paper has been turned into confetti by the scissors of player 1!")
      player1_score += 1
  print()
  print("Player 1 has", player1_score, ", while Player 2 has", player2_score, "!")

  if player1_score == 3 or player2_score == 3: 
    print("Thanks for playing!")
    exit()
  else: 
    continue 
