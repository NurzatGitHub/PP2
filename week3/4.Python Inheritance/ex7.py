#Add Methods

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

#Add a method called welcome to the Student class:

class Students(Person):
    def __init__(self, fname, lname,year):
       super().__init__(fname, lname)
       self.graduationyear = year

    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)
        