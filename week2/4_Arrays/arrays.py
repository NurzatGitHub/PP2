'''
Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
'''
#Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
#Get the value of the first array item:
x = cars[0]
#Modify the value of the first array item:
cars[0] = "Toyota"
#Return the number of elements in the cars array
x = len(cars)
#Delete the second element of the cars array:
cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)
#Print each item in the cars array:
for x in cars:
  print(x)