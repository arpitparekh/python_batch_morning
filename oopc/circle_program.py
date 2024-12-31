# create class called Circle with attributes radius and color
# create method called area and circumference which calculates the area of the circle and circumference of the circle respectively

class Circle:
  radius = 0
  color = ""

  def assignValues(self, r, col):
    self.radius = r
    self.color = col

  def findArea(self):
    print("The area of the circle is:", 3.14 * self.radius * self.radius)

  def findCircumference(self):
    print("The circumference of the circle is:", 2 * 3.14 * self.radius)


c1 = Circle()
c1.assignValues(int(input("Enter the radius of the circle: ")),
                input("Enter the color of the circle: "))
c1.findArea()
c1.findCircumference()
