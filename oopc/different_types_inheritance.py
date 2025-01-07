# single inheritance
# multi level
# heirarchical
# multiple
# hybrid

class Animal:
  type = ""
  color = ""

  def voice(self):
    print("Animal Voice")

class Dog(Animal):
  breed =""
  no_of_leg = 0

  def bark(self):
    print("Dog Bark")

  def display(self):
    print("Type:",self.type)
    print("Color:",self.color)
    print("Breed:",self.breed)
    print("No of Leg:",self.no_of_leg)

class Pug(Dog):
  height = 0.0

  def display(self):
    print("Type:",self.type)
    print("Color:",self.color)
    print("Breed:",self.breed)
    print("No of Leg:",self.no_of_leg)
    print("Height:",self.height)

d = Dog()
d.type = "Mammal"
d.color = "Black"
d.breed = "German Shephard"
d.no_of_leg = 4

d.voice()
d.bark()
d.display()

pug = Pug()
pug.type = "Mammal"
pug.color = "Brown"
pug.breed = "pug"
pug.no_of_leg = 3
pug.height = 1.5

pug.voice()
pug.bark()
pug.display()


