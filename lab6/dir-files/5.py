import os

path = open(r"C:\Users\madik\Desktop\pp2\lab6\dir-files\5ex.txt", "a")
mylist = ["bmw ", "m8 ", "m4 ", "pls."]
for word in mylist:
    path.write(word)