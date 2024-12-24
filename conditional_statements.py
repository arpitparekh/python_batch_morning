# true and false
# conditional statements decide the flow of the program based on the condition given.

name = "Gumit"

# if else
if (name=="Sumit"):
  print("Hello Sumit")
else:
  print("Hello Other")

isLogin = True

if(isLogin):
  print("Welcome")
else:
  print("Please login")

# if elif else

a = 12
b = 20
c = 13

if(a>b):
  print("a is less than b")
elif(a>c):
  print("a is greater than c")
elif(a==c):
  print("a equals c")
elif(a!=c):
  print("a is not equal to c")
else:
  print("other")

# nested if else

x = 12
y = 10
z = 30

if(x>y):
  if(x<z):
    print("x is less than z")
  else:
    print("x is greater than z")
else:
  if(y>z):
    print("y is greater than x and z")

