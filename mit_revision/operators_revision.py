# variable
# datatypes
# int, complex float
# str
# sequential datatypes // list[], tuple(), set{}, dictionary{}
# oprators
# operators are the symbols used to perform operations on variables and values in a program.

# arithmetic operators
# + - * / %  **(power) //(integer division)
a = 12
b = 13
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)

# **
print(a**b)

# % modulus operator (gives reminder)
print(13%5)
print(12 % 8)

print(12 % 13)

print(123 % 10)   # last digit of 123 is 3
print(123 // 10)  # 12 # removes the last digit of 123

# relational operators  # gives boolean value
# < > <= >= == !=

x = 10
y = 20

print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
print(x==y)
print(x!=y)

# logical operators ##  and or not
# used between 2 relational operators

print(x<y and y<x and x==y and x!=y)
print(x<y or y<x or x==y or x!=y)

result = x<y or y<x or x==y or x!=y

print(not result)

# assignment operators
# += -=  *=  /=  //=  %=  **=  =

p = 20
q = 30

p %= 20   # p = p + 20
print(p)
