class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self,x):
    print("Hello my name is " + self.name + x)

p1 = Person("John", 36).myfunc(12)