'''
Check if File exist:
To avoid getting an error, you might want to check if the file exists before you try to delete it:
'''

import os

print(os.path.exists("C:\\Users\\Nurza\\Documents\\PP2\\week6\\1_Directories_files\\3_Python WriteCreat Files\\myfile.txt"))

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")