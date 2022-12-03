print("Welcome to the math game! Today, we're gonna test your multiplication skills, so that you don't fall behind in math class! Let's see how knowledgable you are!")
print() 
math_family= int(input("Your multiples: ->"))

counter = 0 
for i in range (1, 11): 
  correct_answer = i*math_family
  print(i, "x", math_family)
  answer = int(input(">"))
  if answer == correct_answer:
    print("Good job, you got it!")
    counter += 1
  else: 
    print("Sorry, try again!")

if counter == 10: 
  print("OMG, you got it all!! You're truly a mathematician genius!")
else: 
  print(" You got", counter, "out of 10 correct. Next time, aim for a higher score!")
