# type casting

a = 10
print(type(a))

f = float(a)  # type casting from int to float
print(type(f))
print(f)

height = 12.3
print(type(height))

height_int = int(height)
print(type(height_int))
print(height_int)

# str
str = "100"
print(type(str))

str_int = int(str)
print(type(str_int))
print(str_int)

# bool
isLogin = False
print(type(isLogin))

isLogin_int = int(isLogin)
print(type(isLogin_int))
print(isLogin_int)

# int to bool
num = 3
num_bool = bool(num)
print(type(num_bool))
print(num_bool)

# float to bool
num = 0.0
num_bool = bool(num)
print(type(num_bool))
print(num_bool)

# str to bool
str = ""           # false for empty string
str_bool = bool(str)
print(type(str_bool))
print(str_bool)
