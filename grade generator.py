print("Exam grade calculator")
print()
examname = input("Name of the exam: ")
print()
maxposspoints = int(input("Maximum possible points: "))
print()
yourscore = int(input("Your score: "))
print()
gradeearned = float(yourscore / maxposspoints * 100)
finalgrade = round(gradeearned, 2)
if finalgrade >=95: 
  print("You got", finalgrade, "% which is an A")
elif finalgrade >= 90: 
  print("You got", finalgrade, "%, which is an A-")
elif finalgrade >= 87: 
  print("You got", finalgrade, "%, which is a B+")
elif finalgrade >= 83: 
  print("You got", finalgrade, "%, which is a B")
elif finalgrade >= 80: 
  print("You got", finalgrade, "%, which is a B-")
elif finalgrade >= 77: 
  print("You got", finalgrade, "%, which is a C-")
elif finalgrade >= 73: 
  print("You got", finalgrade, "%, which is a C")
elif finalgrade >= 70: 
  print("You got", finalgrade, "%, which is a C-")
elif finalgrade >= 67: 
  print("You got", finalgrade, "%, which is a D+")
elif finalgrade >= 63: 
  print("You got", finalgrade, "%, which is a D")
elif finalgrade >= 60: 
  print("You got", finalgrade, "%, which is a D-")
else: 
  print("You have failed the test completely. Please retake.")

