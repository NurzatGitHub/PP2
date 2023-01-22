thislist = ["apple", "banana", "cherry"]
print(thislist)
'''
 a = [int(i) for i in input().split()]
 if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a)):
        if i == len(a)-1:
            print(a[i - 1] + a[0],end=' ')
        else:
            print(a[i - 1] + a[i + 1],end=" ")
###################################################
a = [int(i) for i in input().split()]
a.sort()
b = []
t = []
if len(a) == 1:
    for i in b:
        print(i)
else:
    for i in range(len(a)):
        if(a[i] == a[i - 1]):
            b.append(a[i])
    t = set(b) 
    for i in t:
        print(i,end=' ')
'''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#################################
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
###########################
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
##############################
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
##############################
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#######################
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
###########################################
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
##################################
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
################################
thislist = ["apple", "banana", "cherry"]
del thislist
######################################
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
############################33
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)