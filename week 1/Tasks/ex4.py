s = input()
t = ''.join(set(s))
print(len(t)/len(s) *100)
string = input()
char_seen = []
for char in string:
    if char not in char_seen:
        char_seen.append(char)
print(''.join(char_seen))