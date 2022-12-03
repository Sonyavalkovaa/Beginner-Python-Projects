myBill = float(input("What was the bill?: "))
tip = int(input("What % do you want the tip?"))
numberOfPeople = int(input("How many people?: "))
answer = float((tip / 100 +1) * myBill) / numberOfPeople 
answer = round(answer, 2)
print("You all owe", answer)