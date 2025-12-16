student=("Mickey",21,"male")
# Count how many times "Mickey" appears
print(student.count("Mickey"))

# Find index of "male"
print(student.index("male"))

# Loop through tuple
for i in student:
    print(i)

# Check if "Bro" is present
if "Bro" in student:
    print("Bro is here!")