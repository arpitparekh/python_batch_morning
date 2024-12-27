# prime number

# num = int(input("Enter a number: ")) # 13  # 2..12


# print("Numer from user is",num)

# flag = 1

# for i in range(2, num):
#   if num%i==0:
#     flag = 0
#     break

# if flag == 1:
#   print("Number is prime")
# else:
#   print("Number is not prime")

# 55
# 2..54

num = int(input("Enter a number: "));flag = 1

for i in range(2, num):
    if num % i == 0:
        flag = 0
        break

print("Number is prime") if (flag == 1)  else print("Number is not prime")





