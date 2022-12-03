print("Fill in the blank lyrics! Type in the blank lyrics and see if you are as cool as me.")
print()
print("You were the _______ to my light")

counter = 1
while True: 
  lyrics = input("Fill in the blank lyrics")
  if lyrics != "shadow": 
    print("Nope, sorry, you didn't get it! Take another shot!")
    counter += 1
  if lyrics == "shadow":      
      print("Yeah, you got it! Go kid!")
      break 