import os
import logger

if not os.path.exists("DemoFolder"):
    os.mkdir("DemoFolder")
    logger.log("DemoFolder created")
    print("DemoFolder created")
else:
    logger.log("DemoFolder already exists")
    print("DemoFolder already exists")
print("Program finished")