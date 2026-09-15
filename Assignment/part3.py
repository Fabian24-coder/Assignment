#Tuples
#Days of the week
daysOfTheWeek = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
print(daysOfTheWeek)
print(f"First day: {daysOfTheWeek[0]}")
print(f"Last day: {daysOfTheWeek[6]}")

daysOfTheWeek[2] = "Unkownday"
#This creates an error since tuples can not be changed, added or removed

#Question: Why is a tuple different from a list? 
    #Elements in Lists can be changed, added or removed while elements in tuples can not be changed, added or removed