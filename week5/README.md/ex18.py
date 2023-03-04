#Search for an upper case "S" character in the beginning of a word, and print the word:

import re

txt = "The rain in Spain Soup"

x = re.search(r"\bS\w+",txt)

print(x.group())