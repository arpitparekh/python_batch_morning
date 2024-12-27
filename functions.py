# functions
# function is block of code that runs when we called it

# function name
# function parameter
# function body
# function return value

# lambda function (anonymous function)(function without name)

def geet():
  print("Hello world")

geet()
geet()
geet()
geet()
geet()

# function with parameter

def geet():
  print("Hello", "Public")

geet()
geet()
geet()
def congrats(name):
  print("Hello", name)

congrats("Arpit")
congrats("Rohan")
congrats("Raj")

def add(n1,n2,n3,n4):
  print("Sum is : => ",n1+n2+n3+n4)

add(1,2,3,4)
add(5,6,7,8)
add(7,8,9,0)


def ra1():
  return 12.34

# if function is returning something the function becomes a variable

print(ra1())
b = ra1()
print(b)

result = 10 + ra1()
print(result)

# with paramter and with return type

def returnRange(start,end):
  list = []
  for i in range(start,end+1):
    list.append(i)
  return list

print(returnRange(1,10))


# for i in returnRange(1,10):
#   print(i)

##################################################################################

# arbitary arguments
# with the use of arbitary arguments we can pass any number of arguments to the function

def take(*args):
  print(args)
  print(args[5])


take(1,12,13,15,16,7,8,9,10)

# keyword arguments

def person(name,age,address):
  print("Name is : ",name)
  print("Age is : ",age)
  print("Address is : ",address)

person(address="Delhi",name="Arpit",age=23)

# default arguments

def sum(a,b=10):
  print(a+b)

sum(12,12)

# keyword arbitary arguments

def company(**kwargs):
  print(kwargs)

company(name="Google",ceo="Sundar Pichai",founder="Larry Page",location="Mountain View",industry="Technology",noOfEmployees=1000,year=1998)

