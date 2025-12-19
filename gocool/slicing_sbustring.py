# Slicing
myString = "mickey mike jebin"
sub1 = myString[0:6]    # characters from index 0 to 5
sub2 = myString[7:]     # from index 7 till end
sub3 = myString[:5]     # from start to index 4
sub4 = myString[10]     # character at index 10
sub5 = myString[-5:]    # last 5 characters

print(sub1)
print(sub2)
print(sub3)
print(sub4)
print(sub5)

# Substring check
if "a" in myString:
    print("a is there")

# Splitting string
words = myString.split("#")
print(words)

# String methods
print(myString.upper())
print(myString.lower())
