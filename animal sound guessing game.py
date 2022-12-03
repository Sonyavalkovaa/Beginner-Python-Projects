exit = "no" 

while exit == "no":
  animalsound = input("What animal do you want to hear?")
  if animalsound == "cow" or animalsound == "Cow": 
    print("Moo") 
  elif animalsound == "donkwy" or animalsound == "Donkey": 
    print("Eeehah")
  elif animalsound == "goat" or animalsound == "Goat": 
    print("Beeeeh")
  elif animalsound == "snake" or animalsound == "Snake": 
    print("Shhhhhh")
  elif animalsound == "horse" or animalsound == "Horse": 
    print("Neaaaaah")
  elif animalsound == "cat" or animalsound == "Cat": 
    print("Meaw")
  elif animalsound == "dog" or animalsound == "Dog": 
    print("Woof")
  else: 
    print(" I do not know this animal sound. Please try again.")

  exit = input("Do you want to exit? ")