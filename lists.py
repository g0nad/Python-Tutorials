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

# Create a new array
shopList2 = ["Bread", "Butter", "Milk"]

# Combine the 2 arrays
print(shopList + shopList2)
# Counts the items on the list or in the array
print(len(shopList + shopList2))
