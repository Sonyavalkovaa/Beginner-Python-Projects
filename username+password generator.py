def login():
  attempt = 0; 
  while attempt < 3:
    attempt += 1
    username = input("What is your username?")
    password = input("What is your password?")
    if username == "Sonya" and password == "Cloud123!":
      print("Welcome to the platform!")
      break
    else: 
      print("Sorry, please try again")  
      continue 
      
print ("Replit login system")
login() 