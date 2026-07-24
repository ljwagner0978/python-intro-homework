students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

top_score = 0
top_score_name = ""
total_score = 0
subject_set = set()
high_scorers = []

for student in students:
    total_score += student["score"]
    subject_set.add(student["subject"])
    if student["score"] > top_score:
        top_score_name = student["name"]
        top_score = student["score"]
    if student["score"] > 75:
        high_scorers.append(student["name"])

print(f"Top scorer:       {top_score_name} ({top_score})")
print(f"Class average:    {total_score/len(students)}")
print(f"Subjects offered: {subject_set}")
print(f"High scorers:     {high_scorers}")