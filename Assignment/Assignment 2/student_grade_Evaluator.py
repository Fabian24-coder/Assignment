count = int(input("How many student entries do you want to create? "))
records = {}

for student in range(count + 1):
    print(f"Entry{student}")
    name = input("Enter student's Name: ")
    score = float(input("Enter score between 0-100"))
    records[name] = score
    passed_count = 0
failed_count = 0
total_score = 0.0

print("\n=======\nEVALUATION RESULTS\n=======")

for name, score in records.items():
    total_score += score
    
    if score >= 70:
        grade = "Grade A"
        status = "Passed with Distinction"
        passed_count += 1
    elif score >= 50:
        grade = "Grade B"
        status = "Passed"
        passed_count += 1
    else:
        grade = "Grade F"
        status = "Needs Improvement"
        failed_count += 1
        
    print(f"{name}: Score {score:.1f} | {grade} | {status}")

# Class Summary
average_score = total_score / count if count > 0 else 0.0

print("\n==========")
print("CLASS PERFORMANCE")
print("==========")
print(f"Average Score: {average_score:.1f}")
print(f"Total Passed: {passed_count}")
print(f"Total Failed: {failed_count}")
print("================")