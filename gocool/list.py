# list = used to store multiple items in a single variable

food = ["pitta", "hamburger", "hotdog", "spaghetti"]

print(food[1])   # hamburger
print(food[3])   # spaghetti
# Print all items using loop
for i in food:
    print(i)
# Update an item
food[0] = "sushi"
print(food[0])   # sushi

# Add items
food.append("ice-cream")
print(food[4])

# Remove items
food.remove("hotdog")   # remove by value
food.pop()              # remove last element
food.pop(1)             # remove element at index 1

# Insert item
food.insert(1, "cake")

# Sort list
food.sort()

# Print all items using loop
for i in food:
    print(i)



# Clear the list
food.clear()