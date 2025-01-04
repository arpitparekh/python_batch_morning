# constructor.py
# constructor is a special method that calls automatically when an object is created. It is used to initialize the object's attributes.
# constructor is defined using __init__() method in the class. but outside of the class, we can call it using the class name followed by parentheses.

class MaroClass:
  def __init__(self,name, age):
    self.name = name
    self.age = age

  def display(self):
    print("Name:",self.name)
    print("Age:",self.age)

m = MaroClass("Sumit", 30)
m.display()
print(m.name)
print(m.age)
