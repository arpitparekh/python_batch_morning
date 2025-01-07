# multiple inheritance in python
# multiple parent and single child class

class Baap1:
  baap1_name = ""
  baap1_age = 0

  def jump(self):
    print("Baap 1 Jump")

class Baap2:
  baap2_name = ""
  baap2_age = 0

  def jump(self):
    print("Baap 2 Jump")


class Child(Baap2,Baap1):
  child_name = ""
  child_age = 0

  def display(self):
    print("Baap1 Name:",self.baap1_name)
    print("Baap1 Age:",self.baap1_age)
    print("Baap2 Name:",self.baap2_name)
    print("Baap2 Age:",self.baap2_age)
    print("Child Name:",self.child_name)
    print("Child Age:",self.child_age)

child = Child()
child.baap1_name = "John"
child.baap1_age = 50
child.baap2_name = "Rock"
child.baap2_age = 45
child.child_name = "Tom"
child.child_age = 10
child.display()

child.jump()
