# operators are the symbols that represent computations like addition and multiplication.

# arithmetic operators

# + - * /  %(modulus)   **(power) //(integer division)
a = 10
b = 20
print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division

c = a/b
print(type(c))

# % modulus reminer

print(12 % 5)  # 0
print(7 % 12)

""" (get the last digit of a number)
12 % 10 = 2
1234 % 10 = 4

"""

# // integral division
print(100//3)

# ** power
print(2**3)
print(3**2)


############### conditional operators ####################

# < > <= >= == !=  # gives boolean value True or False

a = 10
b = 25

print(a<b)
c = a>b
print(type(c))

print(a==b)
print(a!=b)

############### logical operators ####################

# and or not # multiple conditions # True or False

"""
and operator: truth table
True and True = True
True and False = False
False and True = False
False and False = False

or operator: truth table
True or True = True
True or False = True
False or True = True
False or False = False

not operator: truth table
not True = False
not False = True
"""

a = 10
b = 50

print(not(a<b or b > 100))


# assignment operator  # =
# += -= *= /= %= //= **=

num = 12

num += 5
# num = num + 5
print(num)

num %= 55
print(num)

