# squencial data types
# group of values under a single variable name
# 1. list
# 2. tuple
# 3. set
# 4. dict

# list # []
# ordered, mutable ,indexed, allows duplicates

numbers = [1, 2, 3, 4, 5,6,7,8,"Bascom",True,23.343,12 + 3j]
#          0  1  2  3  4
print(numbers)
print(type(numbers))

print(len(numbers))

fruits = ["apple", "banana", "cherry"]
print(fruits)

# accessing elements in list
print(numbers[8])

print(numbers[8:12])   # : range operator

newList = numbers[8:12]
print(newList)

print(numbers[-1])

print(numbers[-12:-8])

print(numbers[0:5:2])  # start : end+1 : step

print(numbers[:4])

print(numbers[4:])

print(numbers[5::2])

# chnage elements in list
height = [12.3, 14.5, 16.7, 18.9]
height[1] = 17.7
print(height)

height[2:4] = [19.9,19.0]
print(height)

# insert elements in list
height.insert(2,999.99)
print(height)

height.append(1000.00)
print(height)

weight = [12.3, 14.5, 16.7, 18.9]
height.extend(weight)
print(height)

# remove elements from list
height.remove(1000.00)
print(height)

height.pop()
print(height)

height.pop(1)
print(height)

# sort the list
height.sort(reverse=False)
print(height)

# copy one list into another
list1= [1,2,3]
list2 = []

list2 = list1

print(list2)

list2[1] = 100
print(list2)

print(list1)

list3 = []
list3 = list1.copy()

print(list3)
list3[1] = 200
print(list3)
print(list1)

# + operator between list
l1 = [1,2,3]
l2 = [4,5,6]
# l3 = l1 + l2
l1.extend(l2)
print(l1)

# empty the list
l1.clear()
print(l1)

# find index of value
l1 = [1,2,3,4,5,6]
print(l1.index(4))

# reverse the list
l1.reverse()
print(l1)

# count the number of occurrences of a value in list
l1 = [1,2,3,4,5,6,2,3,4,5,2,2]
print(l1.count(2))



