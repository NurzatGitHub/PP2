'''
Modify Object Properties
You can modify properties on objects like this:
'''
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
#set the age of p1 to 40:
p1.age = 40
#delet.agee the age property from the p1 object:
del p1.age
#delete the p1 object:
del p1