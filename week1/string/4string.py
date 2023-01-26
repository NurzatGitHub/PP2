a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliq"""
####################SLICING STRING
b = "Hello, World!"
print(b[2:5])
############################
#FROM THE START
b = "Hello, World!"
print(b[:5])
##########################
#Slice To the End
b = "Hello, World!"
print(b[2:])
############################
#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])
###########################Modify Strings
a = "Hello, World!"
print(a.upper())
##########################
a = "Hello, World!"
print(a.lower())
#############################
#replace
a = "Hello, World!"
print(a.replace("H", "J"))
############################
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#######################################
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
###############################
a = "Hello"
b = "World"
c = a + b
print(c)
a = "Hello"
b = "World"
c = a + " " + b
print(c)
############################
####################################format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#####################
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
######################
##############Escape Character
txt = "We are the so-called \"Vikings\" from the north."