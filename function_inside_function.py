# function inside function
# decorators
# generators
# datetime
# scope
# string formatting

# function inside function

# when you create a function inside another function, the inner function is not accessible from outside the outer function. we must have to ruturn the inner function to access it

def outer():
  print("outer function")

  def inner():                   # function creating
    print("inner function")

  return inner  # function is retuning a function

outer()()

def func1():
  def func2():
    def func3():
      print("Nested Function")

    return func3

  return func2

func1()()()

# decorators
# decortors are used to add some functionality to an existing function
# @



# decorator function
def decor(func):
  def wrapper():
    print("Before executing the function")
    func()
    print("After executing the function")

  return wrapper

@decor
def displayingValue():
  print("Displaying Value")

displayingValue()

######################################################################

import time

def myDecor(func):

  def wrapper():
    start_time = time.time()
    func()   # 0.100
    end_time = time.time()
    print("Time taken by function is:", end_time - start_time)


  return wrapper


@myDecor
def printRange():
  for i in range(10000):
    print(i)

printRange()

#########################################################################
# repeate function n times

def repeat(n):
  def decorator(func):
    def wrapper(*args, **kwargs):
      for i in range(n):
        func()
    return wrapper
  return decorator


@repeat(n=5)
def jump():
  print("jump")

jump()


###################################################################

def gen(func):

  def wrapper(a,b):
    if a<b:
      a,b = b,a
    return func(a,b)
  return wrapper


@gen
def sub(a,b):
  return a-b


print(sub(10,20))

######################################################################
