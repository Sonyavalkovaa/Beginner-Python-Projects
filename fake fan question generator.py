activity = input("If you would do one thing for the rest of your life, what would it be?")
if activity == "walking":
  print("That for sure takes a lot of energy!")
  print()
  walking = input ("When do you typically like to walk?")
  if walking == "when stressed out":
    print("that's cool enough")
    print()
    placeofwalking = input("Where do you typically like walking?")
    if placeofwalking == "mountains":
      print("Oh, then you definitely enjoy hiking!")
    else: 
      print("Oh, well, that's also very refreshing!")
elif activity == "reading":
  print("very romantic!")
  print()
  reading = input("What genre of books do you like to read?")
  if reading == "fantasy":
    print("Woo! Diving into books of that sort is very cool! So that means reading fantasy books is your hobby!")
  else: 
    print("Fair enough! Reading books of any genre is cool!")
else: 
  print("Yo, man, you got it!")