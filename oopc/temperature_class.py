# temperature
"""

    Implement a Temperature class that can convert between Celsius and Fahrenheit. Include methods for setting the temperature in either scale and getting the temperature in both scales.
"""

class Temp:
  cel=0
  fan=0

  def assignValues(self,cel,fan):
    self.cel=cel
    self.fan=fan

  def celtofan(self):
    print((self.cel*1.8)+32)

  def fantocel(self):
    print((self.fan-32)/1.8)

t = Temp()
t.assignValues(37,100)
t.celtofan()
t.fantocel()

