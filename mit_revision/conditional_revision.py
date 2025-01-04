# conditional statements
# if else
# if elif else
# nested if else

a = 10

if a>20:
  print("a is less than 20")
else:
  print("a is greater than 20")

# multiple condition checks
# if elif else

num = -45
if num<0:
  print("negative number")
elif num>0:
  print("positive number")
else:
  print("zero")


# nested if else

a = 10
b = 20

if a<b:
  if a>b:
    print("Inner inner if")
  else:
    print("Inner inner else")
else:
  print("Outer else")
