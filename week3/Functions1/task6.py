string = [str(i) for i in input().split()]
#print(string)
def reverse_line(s):
    s.reverse()
    line = str()
    line += str(s[::1])
    print(line) 
    print(*s)
    
reverse_line(string)