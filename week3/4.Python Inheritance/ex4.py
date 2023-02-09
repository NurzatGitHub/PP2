'''
Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
'''

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Students(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

    