with open("A.txt","r") as first,open("B.txt","w") as second:
    for line in first:
        second.write(line)