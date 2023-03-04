# The re module offers a set of functions that allows us to search a string for a match:4

import re
# Returns a list containing all matches
txt = "The rain in Spain"
x = re.findall( "a", txt)
print(x)
print()
# Returns a Match object if there is a match anywhere in the string4

search = re.search("S",txt)
print(search)
print()
# Returns a list where the string has been split at each match

split = re.split("a", txt)
print(split)
print()

# Replaces one or many matches with a string

sub = re.sub("The","a",txt)
print(sub)