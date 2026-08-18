def is_valid_score(score):
    if not score.isdigit():
        return False
    elif int(score) >= 0 and int(score) <= 100:
        return True
    else:
        return False

score = input("Please input a score value: ")
if(is_valid_score(score)):
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")
