def string_test(s):
    d = {"u":0,"l":0}
    for c in s:
        if c.isupper():
            d["u"]+=1
        if c.islower():
            d["l"]+=1
        else:
            pass
    print("Upper",d["u"])
    print("Lower",d["l"])

s = input()
string_test(s)