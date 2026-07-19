#This code takes a hardcoded score value and assigns a corresponding letter grade

score = 71
print(f"Score: {score}")

if score < 60:
    print("Grade: F")
elif score >= 60 and score <=  69:
    print("Grade: D")
elif score >= 70 and score <= 79:
    print("Grade: C")
elif score >= 80 and score <= 89:
    print("Grade: B")
elif score >= 90 and score <= 100:
    print("Grade: A")
else:
    print("Not a valid number.")