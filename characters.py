# class for characters

class FullNames:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Person(FullNames):
  def __init__(self, fname, lname, rank):
    super().__init__(fname, lname)
    self.rank = rank

  def myfunc(self):
    print("Name: " + self.fname, self.lname)
    print("Rank: " + self.rank)
