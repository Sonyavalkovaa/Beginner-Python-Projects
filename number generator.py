print("Welcome to the guessing game")
print() 
print("print any number between 1 and 1000000. If you get it right, you win!")
print()
print("Let's start now!")
print()

import random  
attempt = 1 
myNumber = random.randint(1, 1000000)

while True: 
  guess = int(input("Pick any number between 1 and 1000000"))
  if guess < myNumber: 
    print("that number is way too low. Try again!")
    print()
    attempt += 1 
  elif guess > myNumber: 
    print("Okay, man, that's too high. Take another shot!")
    print()
    attempt += 1 
  elif guess == myNumber: 
    print("Yay, you got it!") 
    break 
  else: 
    print("What on earth is this number?!") 
print ("It took you", attempt, "attempts to get the right answer! Next time, try to beat your score!")