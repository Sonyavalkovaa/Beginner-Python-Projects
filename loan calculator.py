loan = 1000
apr= 0.05 
for k in range(10):
  loan+=(loan*apr)
  print("Year", k+1, "is",
round(loan, 2))