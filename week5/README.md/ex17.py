# Print the string passed into the function:encoding="utf-8"
import re
# date = open(r"C:\Users\Nurza\Documents\PP2\week5\regex.md\row.txt",errors="ignore")
# f = date.read()

txt = "The rain in Spain"

x = re.search(r"\bS\w+",txt)

print(x.string)