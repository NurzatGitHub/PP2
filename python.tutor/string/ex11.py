
def myfun(line):
    a = line.find('h')
    b = line.rfind('h')
    if a == -1:
        return line
    elif a == b:
        return line.replace('h','H')
    l = str()
    for i in range(a + 1):
        l += line[i]
    for i in  range(a + 1,b):
        if line[i] == 'h':
            l += 'H'
        else:
            l += line[i]
    for i in  range(b,len(line)):
        l += line[i]
    return l
s = input()
print(myfun(s))