color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open(R'C:\Users\Nurza\Documents\PP2\week6\1_Directories_files\dir-and-files.md\myfolder\myfile1.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open(R'C:\Users\Nurza\Documents\PP2\week6\1_Directories_files\dir-and-files.md\myfolder\myfile1.txt')
print(content.read())