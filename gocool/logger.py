def log(message):
    f = open("log.txt", "a")
    f.write(message + "\n")
    f.close()