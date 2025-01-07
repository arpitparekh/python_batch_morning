# varso
#inheritance
# when child class object use parent class properties and methods, it is called inheritance.

class Person:  # base class # parent class # super class
  name = ""
  age = 0

class Student(Person):  # derived class # child class # sub class
  roll_no = 0
  marks = 0

  def display(self):
    print("Name:",self.name)
    print("Age:",self.age)
    print("Roll No:",self.roll_no)
    print("Marks:",self.marks)

s1 = Student()
s1.name = "John"
s1.age = 20
s1.roll_no = 101
s1.marks = 90
s1.display()


class Parent:
  parent_name = ""
  parent_age = 0

class Child:
  pass

