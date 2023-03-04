import re

file  = open(r"C:\Users\Nurza\Documents\PP2\week5\row.txt",encoding="utf-8")

x = re.findall(".*a.*b{2,3}",file.read())

print(x)