'''
Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
'''

class Student(Person):
  pass

#Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")
x.printname()
