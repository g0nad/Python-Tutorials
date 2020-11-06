# Defines the list or array
shopList = ["Apples", "Oranges", "Bananas", "Peaches"]
# Prints the first item
print(shopList[0])
# Prints items 0, 1, 2
print(shopList[0:3])
# Adds a new item to the array
shopList.append("Blueberries")
# Prints the entire array
print(shopList)
# Prints the shopping list minus Blueberries
print(shopList[:-1])
# Prints the shopping list minus Peaches and Blueberries
print(shopList[:-2])
# Replaces Apples with Cherries
shopList[0] = "Cherries"
print(shopList)
# Deletes Oranges
del shopList[1]
print(shopList)
# Counts the items on the list or in the array
print(len(shopList))

# This is a list
students = ["Ethan", 16, "Elizabeth", 13]
print(students[0])

# This is the same data in a dictionary
students = {"Ethan": 16, "Elizabeth": 13}

# How to get the age by looking up the key
students["Ethan"]

# How to update an age using the key
students["Ethan"] = 15

# Delete a key from the dictionary
del students["Elizabeth"]
students

# how many students are in the dictionary
len(students)
