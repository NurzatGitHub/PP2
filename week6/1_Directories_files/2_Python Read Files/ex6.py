# Close Files
# It is a good practice to always close the file when you are done with it.

f = open(r"C:\Users\Nurza\Documents\PP2\week6\1_Directories_files\1_Python File Open\demofile.txt","rt")
print(f.readline())
f.close()