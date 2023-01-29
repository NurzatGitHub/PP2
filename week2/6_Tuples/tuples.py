#Print the first item in the fruits tuple
fruits = ("apple", "banana", "cherry")
print(fruits[0])
print('\n')
#Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))
print('\n')
#Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
print('\n')
#Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

print('\n')
#Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#Use the add method to add "orange" to the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#Use the correct method to add multiple items (more_fruits) to the fruits set.

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)