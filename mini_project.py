#This code takes the user's inputted day and time of day value and prints a suggested activity depending on the day and time of day

while True:
 day = (input("What day is it?: ")).capitalize()
 phase = (input("What time of day?: ")).capitalize()
 
 try:
  
  days_of_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  time_of_day_array = ["Morning", "Afternoon", "Evening"]

  if day not in ("Monday","Tuesday","Wednesday","Thursday", "Friday", "Saturday", "Sunday"):
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")
    break
  if phase not in ("Morning", "Afternoon", "Evening"):
    print("Sorry, I don't recognize that time. Try: Morning, Afternoon, or Evening")
    break
  
  a = ""
  if day in ("Monday","Tuesday","Wednesday") and phase == "Morning":
    a = ("It's morning time! Get to work!")
  elif day == "Thursday" and phase == "Morning":
    a = ("Its Thursday morning, definitely skip work and all other obligations.")
  elif day == "Friday" and phase == "Morning":
    a = ("Its Friday morning, weekend coming up!. Fantasize about your weekend plans.")
  elif day in ("Saturday","Sunday") and phase == "Morning": 
    a = ("Its the weekend! Go for a stroll or have a hot cup of Joe.")
  elif day in ("Monday","Tuesday","Wednesday","Thursday") and phase == "Afternoon":
    a = ("Afternoon time! Play games with friends or go to the gym. Rest and relax.")
  elif day == "Friday" and phase == "Afternoon":
    a = ("Weekend time! Go splurge on some dinner, you deserve it!")
  elif day in ("Saturday", "Sunday") and phase == "Afternoon":
    a = ("The world is your oyster. Go travel, hang out with old friends and make new ones!")
  elif day in ("Saturday", "Sunday", "Friday") and phase == "Evening":
    a = ("Perfect night for a movie or trying a new recipe.")
  elif day in ("Monday","Tuesday","Wednesday","Thursday") and phase == "Evening":
    a = ("Read or book, doomscroll, or prep for bed. You got work tomorrow.")
  else:
    print("Sorry, I dont recognize that time.")
    a = ("Incorrect phase value inputted")

  print(f"Suggestion: {a}")
  break
 except ValueError:
    print("Sorry, I don't recognize that day or time. Please try again.")
