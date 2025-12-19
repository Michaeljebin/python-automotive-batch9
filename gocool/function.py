marks = [] 
for i in range(5):
    m = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

def calculate(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def score(marks):
    for i in range(len(marks)):
        if marks[i] < 0 or marks[i] > 100:
            print("invalid input")
        elif marks[i] >= 50:
            print("The student is pass")
        else:
            print("The student is fail")

total, average = calculate(marks)
score(marks)

print("\nTotal Marks:", total)
print("Average Marks:", average)