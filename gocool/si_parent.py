from si_child import simple_interest
from calculator1 import calculator
print("1. Simple Interest")
print("2. Calculator")

choice = int(input("Enter your choice: "))

if choice == 1:
    simple_interest()
elif choice == 2:
    calculator()
else:
    print("Invalid choice")