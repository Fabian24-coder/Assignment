# Question 9: Student Management Data

# Create a dictionary containing data for 3 students
students = {
    "student1": {
        "name": "Franco",
        "age": 22,
        "course": "Backend Development",
        "skills": ["Python", "HTML", "Git"]
    },
    "student2": {
        "name": "Mary",
        "age": 24,
        "course": "Data Analysis",
        "skills": ["Excel", "SQL", "Python"]
    },
    "student3": {
        "name": "Alex",
        "age": 21,
        "course": "Cybersecurity",
        "skills": ["Linux", "Networking", "Python"]
    }
}

# Print the information for all students
for student_id, details in students.items():
    print(f"\nID: {student_id}")
    print(f"Name: {details['name']}")
    print(f"Age: {details['age']}")
    print(f"Course: {details['course']}")
    print(f"Skills: {', '.join(details['skills'])}")

print("\n")
# Student Information Variables
student_name = "Buni"   
student_age = 19              
student_height = 1.23         
is_enrolled = True            

# list containing of at least 5 programming languages
programmingLanguage = ["Python", "HTML", "CSS", "JavaScript", "Java"]
print(f"Initial list: {programmingLanguage}")

# 2.first item
print(f"First item: {programmingLanguage[0]}")

# 3. new item
programmingLanguage.append("Java")
print(f"After adding 'Java': {programmingLanguage}")

# 4. Remove one item
programmingLanguage.remove("CSS")

# 5.the updated list
print(f"Updated list after removing 'CSS': {programmingLanguage}")


#2. Tuple 

# Tuple containing 3 favorite numbers
favNumbers = (7, 10, 25)

# Display second number
print(f"\nSecond favorite number: {favNumbers[1]}")


#3. Set

hobbies = {"Reading", "Gyming", "Football", "Reading"}

print(f"\nHobbies set: {hobbies}")

print("Note: Sets automatically remove duplicate elements, that is why 'Reading' appeared once.")

# Added new hobby
hobbies.add("Photography")
print(f"Updated hobbies set after adding 'Photography': {hobbies}")


#4. Dictionary
student_profile = {
    "name": student_name,
    "age": student_age,
    "height": student_height,
    "is_enrolled": is_enrolled,
    "skills": programmingLanguage,
    "favNumbers": favNumbers,
    "hobbies": hobbies
}

#student's name
print(f"\nStudent Name: {student_profile['name']}")

#student's skills
print(f"Student Skills: {student_profile['skills']}")

# Added new key called "country"
student_profile["country"] = "Uganda"

# Update student's age
student_profile["age"] = 26

#complete dictionary
for key, value in student_profile.items():
    print(f"  {key}: {value}")



# Bonus Challenge
myName = "Alioma Franco"
myAge = 20
favLanguage = "Python"

#Dictionary
user_info = {
    "name": myName,
    "age": myAge,
    "favoriteLanguage": favLanguage
}

#formatted output 
print(f"\nHello {user_info['name']}!")

print(f"You are {user_info['age']} years old.")

print(f"Your favorite programming language is {user_info['favoriteLanguage']}.")