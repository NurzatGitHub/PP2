import os

f  = "C:\\Users\\Nurza\\Documents\\PP2\\week5"

# print(os.path.dirname(f))
# if os.path.exists(f):
#     if os.path.isdir(f):
#         for fol in f:
#             if os.path.isdir(fol):
#                 print(os.path.dirname(fol))

for root, directories, files in os.walk(f):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)