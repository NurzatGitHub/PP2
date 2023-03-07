# By looping through the lines of the file, you can read the whole file, line by line:

f = open(r"C:\Users\Nurza\Documents\PP2\week6\1_Directories_files\1_Python File Open\demofile.txt","rt")
for x in f:
  print(x,end=' ')