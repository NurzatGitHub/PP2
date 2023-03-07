f = open(r"C:\Users\Nurza\Documents\PP2\week6\1_Directories_files\1_Python File Open\demofile.txt", "w")
f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
f = open(r"C:\Users\Nurza\Documents\PP2\week6\1_Directories_files\1_Python File Open\demofile.txt", "r")
print(f.read())

