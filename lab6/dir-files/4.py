import os

filename = open(r"C:\Users\madik\Desktop\pp2\lab6\dir-files\4ex.txt")
count = 0
for lines in filename:
    count += 1
print(f"File has {count} lines.")    