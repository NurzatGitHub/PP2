import re

with open(r"C:\Users\Nurza\Documents\PP2\week5\row.txt",encoding="utf-8") as file:
    find = file.read()

x = re.findall(".*a.*b.*",find)
print(x)