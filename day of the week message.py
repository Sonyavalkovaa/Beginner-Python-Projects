Name= input("Name ->")
print("Hi", Name, ",","hope it's all going well for you!")
print()
hobby= input("What is your most beloved hobby?")
print()
food = input("What is your favorite go-to food?")
print()
dayofweek= input("What's the day of the week today?") 
if dayofweek == "Monday" or dayofweek == "monday" and hobby == "school" and food == "hamburger":
  print("I can totally understand that coming back to school after a weekend break may not seem satisfying. However, school is important, you lazy guy! Make sure that you dive right into the day with schoolwork and studies! Oh, and also- eating hamburgers every Monday is not healthy for you, it will negatively affect your studies!") 
  if dayofweek == "Monday" or dayofweek == "monday" and hobby == "lacrose" and food == "fried egg":
    print("Yo, starting off with lacrose on a Monday is pretty energizing, it must give you an amazing kickstart for the school week! And fried egg will definitely help you stay awake! However, would you please give me a taste as well? I'm very hungry, yum!")
elif dayofweek == "Tuesday" or dayofweek == "tuesday" and hobby == "school" and food == "hamburger":
  print("Hope your Monday studies went well for you! Keep the pace up, the week hasn't ended yet! And you should really cut out on those hamburgers!")
elif dayofweek == "Wednesday" or dayofweek == "wednesday" and hobby == "school":
  print("Yeah,", Name, "let's go! Working hard, playing hard there! It may be tiring already, but remember- two more days left until the end of the school week!")
  if dayofweek == "Wednesday" or dayofweek == "wednesday" and food == "fried egg":
    print(Name, ",", "seems like fried eggs really helped you get over with the first three days of the school week!")
elif dayofweek == "Thursday" or dayofweek == "thursday" and hobby == "school":
  print("Yo, stop skipping classes there! There's not much left there, only two more days!")
  if dayofweek == "Thursday" or dayofweek == "thursday" and food == "hamburger":
    print("Bro, you're really gonna die from so many hamburgers!")
elif dayofweek == "Friday" or dayofweek == "friday" and hobby == "school":
  print("Finally, you've made it! Even though you, dumb head, have skipped a few classes, you've still finished off strong! Good work there. However, don't be too proud of yourself, and keep it up!")
elif dayofweek == "Saturday" or dayofweek == "saturday" and hobby == "school":
  print("Hey, get up now! Though there's no school today, you might want to tidy up your studies!")
  if dayofweek == "Saturday" or dayofweek == "saturday" and food == "hamburgers":
    print("Nuh-ugh, no good eating hamburgers all day!")
elif dayofweek == "Sunday" or dayofweek == "sunday" and hobby == "school":
  print("Yo, you might wanna take a break from schoolwork today, since tomorrow wil be another school week!")
  if dayofweek == "Sunday" or dayofweek == "sunday" and food == "fried egg":
    print("Fried eggs are always good, but how about eating something else? I'd throw up by this time if I'd eat fried eggs all week long!")
else: 
  print("Well, I guess you just have a good day out there! May", hobby, "and", food, "be your helpers for the day!")

