names = ["michael", "Ayan","Arnab"]
age1, age2, age3 = 21, 22, 23
contact1,contact2,contact3, = 1234567890,1234512345,1234123412
weight1,weight2,weight3 = 70.6,50.3,60.3
print("Name %s" % names[0],names[1],names[2])
print("Age %d" % age1,age2,age3)
print("contact %.2f" % contact1,contact2,contact3)
print(" Weight %.2f" % weight1,weight2,weight3)
print("Name : %s" % names[0],  "Age : %d" % age1,"contact :%.2f" % contact1)
print("Name : %s" % names[1],  "Age : %d" % age2,"contact :%.2f" % contact2)
print("Name : %s" % names[2],  "Age : %d" % age3,"contact :%.2f" % contact3)
print("Name : %s\nAge : %d\nConntact: %f\nWeignt : %.2f\n" % (names[0],age1,contact1,weight1))