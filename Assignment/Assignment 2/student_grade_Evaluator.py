count = int(input("How many student entries do you want to create? "))
records = {}

for student in range(count):
    print(f"Entry {student + 1}")
    name = input("Enter student's Name: ")
    score = float(input("Enter score: "))
    records[name] = score
    passedStudentNumber = 0
    failedStudentNumber = 0
    totalScore = 0.0

print(("="*20) + "\nEVALUATION RESULTS\n" + ("="*20))

for name, score in records.items():
    totalScore += score
    
    if score >= 70:
        grade = "Grade A"
        status = "Passed with Distinction"
        passedStudentNumber += 1
    elif score >= 50:
        grade = "Grade B"
        status = "Passed"
        passedStudentNumber += 1
    else:
        grade = "Grade F"
        status = "Needs Improvement"
        failedStudentNumber += 1
        
    print(f"Name: {name}\nScore: {score:.1f}\nGrade: {grade}\nComment: {status}")

# Class Summary
averageScore = totalScore / count 

print("="*20)
print("CLASS PERFORMANCE")
print("="*20)
print(f"Average Score: {averageScore:.1f}")
print(f"Total Passed: {passedStudentNumber}")
print(f"Total Failed: {failedStudentNumber}")