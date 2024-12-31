# class object
# oopc
# object oriented programming concepts
# functional programming
# object oriented programming  # dividing a code into classes and objects

# class
# object

class Student:  # blueprint

  # properties(variables) # methods(memer functions)
  # multiple datatypes under single variable name

  name= ""
  age = 0
  marks = []


  def learning(self):
    print("students are learning")

s1 = Student()  # object
s1.name = "Arpit"
s1.age = 23
s1.marks = [12,34,56,78]

s2 = Student()
s2.name = "John"
s2.age = 24
s2.marks = [12,34,56,78]

s3 = Student()
s3.name = "John"
s3.age = 24
s3.marks = [12,34,56,78]

s4 = Student()


for i in [s1,s2,s3,s4]:
  print(i.name, i.age, i.marks)
  i.learning()


