import os

f = r"C:\Users\Nurza\Documents\PP2\week6\1_Directories_files\dir-and-files.md\C.txt"

if os.path.exists(f):
    print("file",os.path.basename(f),"deleted")
    os.remove(f)