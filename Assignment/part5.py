#Dictionary
#8. Student Profile
student = {"name": "Alioma Franco Buni",
            "age": 17,
            "course": "Backend",
            "level": "Intermediate",
            "skills": "Frontend, Data analyst"}

print(student)
print(f"Student Name: {student['name']}")

student.update({"email": "email@fake.com"})

student.update({"level": "Beginner"})

student.pop("age")

print(f"New Student Profile: {student}")