mySet = {"Michael", "Ayan", "arnan","ankitha","shurthi"}
print(mySet)

# Creating a list
myList = ['a', 'b']
print(myList)

# Creating another set
mySet2 = {"a", "n"}

# Empty set
empty_set = set()
print(type(mySet))      # data type of mySet
print(type(empty_set))  # data type of empty set

# Adding and removing elements in a set
mySet.add("Mickey")
mySet.discard("Mike")

# Updating set with list elements
mySet.update(myList)

# Count of elements in set
count = len(mySet)
print("Count:", count)

# Union
print("Union:", mySet | mySet2)

# Intersection
print("Intersection:", mySet & mySet2)

# Iterating through set
for fruit in mySet:
    print(fruit)

