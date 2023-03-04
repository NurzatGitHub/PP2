import re

file = open(r"C:\Users\Nurza\Documents\PP2\week5\row.txt",encoding="utf-8")

def snake_to_camel(word):
    return ''.join(x.capitalize() or '_' for x in word.split('_'))


print(snake_to_camel(file.read()))