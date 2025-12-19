#G7. Pattern Printing
#Write a program that takes an integer n as input and prints a right-angled triangle star pattern of height n using nested loop

#getting input from the user
n = int(input("Enter the height:"))
 #Looping statement
for i in range (n):  
##nested looping Statement 
    for j in range (i+1): 
        print("*",end=" ")
    print()