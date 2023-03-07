'''
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file

"w" - Write - will overwrite any existing content
'''

f = open(r"C:\Users\Nurza\Documents\PP2\week6\1_Directories_files\1_Python File Open\demofile.txt","a")

f.write("Now the file has more content!")
f.close()

# open and the file after the appending

f = open(r"C:\Users\Nurza\Documents\PP2\week6\1_Directories_files\1_Python File Open\demofile.txt")

print(f.read())