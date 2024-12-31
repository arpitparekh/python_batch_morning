# lambda functions
# lambda function is anonymous function(function without name)

# def sum(a,b):
#   return a+b


result =  lambda a,b : a+b

print(result(12,12))

# lambda function is used to create a higher order function
# higher order function is a function which takes function as a parameter
# or returns a function as a result

def func(data):
  print(data(10))

func(lambda x : x+10)   # function as parameter (lambda function in a parameter)


def calculation(a,b,func):

  print(func(a,b))

calculation(10,20,lambda x,y : x/y)

# lambda function is used to extends the functionality of a function

def maruFunction():
  return lambda a : a+10

print(maruFunction()(10))

# numpy library has a function called "vectorize" which can be used to convert a function to a vectorized function

# map function
nums = [1,6,9,7,4,3,6,8,9,6,4,4]  # 12


# for i in range(0,len(list)):
#   list[i] = list[i] + 10

print(list)

res= map(lambda x : x*10,nums)

print(list(res))
