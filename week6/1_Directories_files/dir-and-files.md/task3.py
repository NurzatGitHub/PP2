import os
f  = "C:\\Users\\Nurza\\Documents\\PP2\\week5\\row.txt"

if os.path.exists(f):
    if os.path.isdir(f):
        print(os.path.dirname(f))
    else:
        print(os.path.basename(f))