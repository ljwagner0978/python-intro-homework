student = {
    "name": "Sarah",
    "grade": "A",
    "subjects": ["Chemistry", "Biology", "English"]
}

for x in student.items():
    print(x)

student["graduated"] = False

print(student)