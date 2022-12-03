import random 
print("The Infinity Dice")

sides= int(input("How many sides does your dice have?"))
playgame = "yes"

def rollDice(sides):
  result= random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6) 
  rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice 
  return health

print("Character Image Generator")

HaveACharacter = "yes"

while HaveACharacter == "yes":
  character = input ("Name your character: ")
  health = str(roll_6_and_8())
  print("Their health is", health, "hp")
  HaveACharacter = input ("Would you like to create another character?")
  