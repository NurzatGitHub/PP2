def polindrom(s):
    t = s[::-1]
    if s == t:
        return True
    else:
        return False
s = input()

print(polindrom(s))