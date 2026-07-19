#This code takes the user's inputted day and time of day value and prints a suggested activity depending on the day and time of day

day = (input("What day is it?: ")).lower()
time = (input("What time of day?: ")).lower()

if day not in ("monday","tuesday","wednesday","thursday", "friday", "saturday", "sunday"):
  print("Sorry, I don't recognize that day. Please try again.")
elif time not in ("morning", "afternoon", "evening"):
  print("Sorry, I don't recognize that time. Please try morning, afternoon, or evening.")
elif day == "monday" and time == "morning":
  print("Suggestion: It's morning time! Get to work!")
elif day =="monday" and time == "afternoon":
  print("Suggestion: Take a break, play some online chess!")
elif day =="monday" and time == "evening":
  print("Suggestion: Read or book and prep for bed. You got work tomorrow.")
elif day == "tuesday" and time == "morning":
  print("Suggestion: Get ready for work and remember to appreciate the small things!")
elif day == "tuesday" and time == "afternoon":
  print("Suggestion: Afternoon time! Play games with friends or go to the gym. Rest and relax.")
elif day == "tuesday" and time == "evening":
  print("Suggestion: Watch a tv show! Try not to binge it!")
elif day == "wednesday" and time == "morning":
  print("Suggestion: Hump day! Research a fun fact!")
elif day == "wednesday" and time == "afternoon":
  print("Suggestion: Go splurge on some dinner, you deserve it!")
elif day == "wednesday" and time == "evening":
  print("Suggestion: Take a nice cool bath!")
elif day == "thursday" and time == "morning":
  print("Suggestion: Its thursday morning, Friday coming up soon!.")
elif day == "thursday" and time == "afternoon":
  print("Suggestion: Have a good time with friends!")
elif day == "thursday" and time == "evening":
  print("Suggestion: Read a book and write down what you like about it!")
elif day == "friday" and time == "morning":
  print("Suggestion: Its friday morning, weekend coming up!. Fantasize about your weekend plans.")
elif day == "friday" and time == "afternoon":
  print("Suggestion: Celebrate with a brisk break! Your weekend is here!")
elif day == "friday" and time == "evening":
  print("Suggestion: Perfect night for a movie with friends.")
elif day == "saturday" and time == "morning": 
  print("Suggestion: Its the weekend! Go for a stroll or have a hot cup of Joe.")
elif day == "saturday" and time == "afternoon":
  print("Suggestion: The world is your oyster. Go travel, hang out with old friends and make new ones!")
elif day == "saturday" and time == "evening":
  print("Suggestion: Enjoy a night indoors with a nice beverage.")
elif day == "sunday" and time == "morning":
  print("Suggestion: Go to church or practice spirtuality in any form you like.")
elif day == "sunday" and time == "afternoon":
  print("Suggestion: Go appreciate the beauty of nature.")
elif day == "sunday" and time == "evening":
  print("Suggestion: Prepare for work tomorrow! Go to sleep early.")

else:
   print("I do not have a suggestion for this Day/Time. Try again please!")
