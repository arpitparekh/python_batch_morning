# tuple is a collection of elements of different data types
# tuple is immutable # unchangeable # readonly
# indexed # ordered # allows duplicates
# ()

vegitables = ('carrot', 'potato', 'tomato', 'onion', 'pepper')
# vegitables[0] = 'cabbage'  not possible in tuple

print(vegitables[0])
print(vegitables[1])

print(len(vegitables))

print(type(vegitables))

vegitables = list(vegitables)

print(type(vegitables))
vegitables[0] = 'cabbage'
print(vegitables)

vegitables = tuple(vegitables)
print(vegitables)
