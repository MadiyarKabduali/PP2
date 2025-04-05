import os

path = (r"C:\Users\madik\Desktop\pp2\lab6\dir-files\deletefile.txt")
if os.path.exists(path):    
    os.remove(path)
else:
    print("This file doesn't exist.")