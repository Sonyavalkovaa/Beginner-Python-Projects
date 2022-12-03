import random 
print("The Infinity Dice")

sides= int(input("How many sides does your dice have?"))
playgame = "yes"

def rollDice(sides):
  print("you rolled", random.randint(1,sides))
while playgame == "yes":
  rollDice(sides)
  playgame = input("Do you want to roll again?")