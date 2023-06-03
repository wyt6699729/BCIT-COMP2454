# Excercise 1
list = [1.3, 2.6, 8.9, 11.5, 14.8]
print(f"The array length is {str(len(list))}.")

for index in range(len(list)):
    print(f"index {index}: {list[index]}")

print("Here is the list again")

for item in list:
    print(item)

# Excercise 2
def showFruitList(fruitList):
    print("\n***DISPLAYING ARRAY CONTENTS***")
    for i in range(len(fruitList)):
        print(fruitList[i])
# Create array
fruit = ["apple"]

# Add items to array
fruit.append("pears")
fruit.insert(0, "plums")

# Sort array
fruit.sort()

# Show array contents
showFruitList(fruit)

# Excercise 3
moreFruits = ["bananas", "dates", "peaches"]
fruit.extend(moreFruits)
showFruitList(fruit)
