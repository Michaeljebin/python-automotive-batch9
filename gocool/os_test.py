#Write a Python program that combines os and a user-defined package to:
#Create a project directory structure
#se a package function to log the directory creation details into a file

import os
os.mkdir("DemoFolder")
f = open("log.txt", "a")
f.write("DemoFolder created\n")
f.close()

print("Done")