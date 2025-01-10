def maruFunction():
  x = 20   # local scope
  print(x)


y = 30   # global scope

def foo():
  global y   # to access global inside a function
  y = 70
  print(y)


foo()
print(y)




