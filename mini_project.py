#This code takes the user's inputted day and time of day value and prints a suggested activity depending on the day and time of day


 day = (input("What day is it?: ")).strip.lower()
 time = (input("What time of day?: ")).strip.lower()

 if day not in ("monday","tuesday","wednesday","thursday", "friday", "saturday", "sunday"):
   print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")
 elif time not in ("morning", "afternoon", "evening"):
   print("Sorry, I don't recognize that time. Try: morning, afternoon, or evening")
 elif day in ("monday","tuesday","wednesday") and time == "morning":
   print("Suggestion: It's morning time! Get to work!")
  elif day == "thursday" and time == "morning":
   print("Suggestion: Its thursday morning, definitely skip work and all other obligations.")
  elif day == "friday" and time == "morning":
   print("Suggestion: Its friday morning, weekend coming up!. Fantasize about your weekend plans.")
  elif day in ("saturday","sunday") and time == "morning": 
   print("Suggestion: Its the weekend! Go for a stroll or have a hot cup of Joe.")
  elif day in ("monday","tuesday","wednesday","thursday") and time == "afternoon":
   print("Suggestion: Afternoon time! Play games with friends or go to the gym. Rest and relax.")
  elif day == "friday" and time == "afternoon":
   print("Suggestion: Weekend time! Go splurge on some dinner, you deserve it!")
  elif day in ("saturday", "sunday") and time == "afternoon":
   print("Suggestion: The world is your oyster. Go travel, hang out with old friends and make new ones!")
  elif day in ("saturday", "sunday", "friday") and time == "evening":
   print("Suggestion: Perfect night for a movie or trying a new recipe.")
  elif day in ("monday","tuesday","wednesday") and time == "evening":
   print("Suggestion: Read or book, doomscroll, or prep for bed. You got work tomorrow.")
  elif day == "thursday" and time == "evening":
   print("Suggestion: Have some cake! Tomorrow's Friday!")
  else:
   print("Suggestion: Redo this!")
