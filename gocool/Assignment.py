#getting input from the user
n = int(input("Enter the height:"))
for i in range (n):#Looping statement
    for k in range (i,n): ##nested looping(1,n)reverse pattern
        print(" ",end="")
    for j in range (i+1): # Nested Looping(i+1)normal pattern
        print("*",end=" ")
    print()