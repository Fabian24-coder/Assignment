#Favorite foods
favorite_foods = ["Rice", "chicken", "cassava","Meat", "Pizza"]

    #Print the entire list.
print(favorite_foods)
    #2. Print the first and last food.
print(favorite_foods[0], favorite_foods[4])
    #3. Add one more food.
favorite_foods.append("Banana")
    #4. Remove one food.
favorite_foods.remove("Pizza")
    #5. Change one food to another food.
favorite_foods[2] = "Mutton"
    #6. Print the final list.
print(favorite_foods)

#4. Student scores
scores = [75, 80, 65, 90, 85]
print(scores)
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
scores.append(95)
print(f"Updated scores: {scores}")