#sets
#6. Remove duplicates values
numbers = [1, 2, 3, 4,2, 5,3,6, 1]
newSet = set(numbers)
print(f"Result: {newSet}")

#Explain why some values disappeared. 
    #This is because sets do not allow duplicate values, so when the list was converted to a set, the duplicates were removed.

#7. Unique programming languages
languages = ["Python", "Java", "Python", "C++", "JavaScript", "Python"]

newSet = set(languages)
print(f"Unique Programming Languages: {newSet}")

newSet.add("Django")
