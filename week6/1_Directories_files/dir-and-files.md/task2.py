import os

f  = "C:\\Users\\Nurza\\Documents\\PP2\\week5"
print('Exist:',os.access(f,os.F_OK))
print('Readable:',os.access(f,os.R_OK))
print('Writable:',os.access(f,os.W_OK))
print('Executable',os.access(f,os.X_OK))