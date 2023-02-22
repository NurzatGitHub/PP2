'''
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:
'''

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))