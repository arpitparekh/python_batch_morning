# set
# unordered, mutable, no duplicates

numbers = {1, 12, 3, 4, 99,5, 6, 7, 8, 9, 10,1,2,3}
print(numbers)
print(type(numbers))

# insert value in set
numbers.add(11)
print(numbers)

values = {77,66,55}
numbers.update(values)
print(numbers)

# remove and discard
numbers.discard(100)
print(numbers)

numbers.pop()
print(numbers)


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
# print(set1.union(set2))
print(set1 | set2)
# print(set1.intersection(set2))
print(set1 & set2)
print(set1.difference(set2))
print(set1 - set2)

# forzen set
frozen_set = frozenset({1,2,3,4,5})
print(frozen_set) # readonly set

tuple1 = tuple(set1)  # also usig typecasing
