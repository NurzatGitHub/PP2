#Loop through the items in the fruits list.
fruits = ['apple','banana','cherry']
for x in fruits:
    print(x)

print('\n')

#In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
       continue
    print(x)

print('\n')
#Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
    
        break
    print(x)