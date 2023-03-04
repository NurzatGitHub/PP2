'''
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:
'''

import re

txt = "The rain in Spain"

x = re.search('\s',txt)
print(x.start())
print(x.end())