# loops in python

# for loop
# while

# num = int(input("Enter a number: "))  # 100
# num = 10

for i in range(1,11): print(i)

for i in range(1,11,2): # start,end+1,step
  print(i)

for i in range(10,2,-1):  # for reverse loop
  print(i)

# print all the odd number between 1 and 1000

for i in range(1,1001): print(i) if i % 2 == 1 else None

# while
a = 1

while a<10:
  print(a)
  a+=1
