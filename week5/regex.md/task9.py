import re

file = open(r"C:\Users\Nurza\Documents\PP2\week5\text.txt",encoding="utf-8")

x = re.findall("[A-Z][a-z]*",file.read())

print(' '.join(x))