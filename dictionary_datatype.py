# dictionary datatypw is a collection of key-value pairs
userData = {              # json
  "name":"Sumit",
  "age":30,
  "email":"sumit@gmail.com",
  "marks":[70,80,90],
  (1,2,3):"tuple as key",
  "isStudent":True,
  "address":{
    "city" : "New York",
    "state" : "NY",
    "country" : "USA"
  },
  "name":"Gumit",
}


"""

"{              # json
  "name":"Sumit",
  "age":30,
  "email":"sumit@gmail.com",
  "marks":[70,80,90],
  (1,2,3):"tuple as key",
  "isStudent":True,
  "address":{
    "city" : "New York",
    "state" : "NY",
    "country" : "USA"
  },
}"


"""

print(userData)
print(type(userData))
print(userData["name"])
print(userData["address"]["city"])

userData["address"]["city"] = "Pune"

print(userData)

print(len(userData))

# set and dictionary are unordered
values = {}                    # dictionary
print(type(values))

# empty set
values = set()
print(type(values))

userData["height"] = 12.3

print(userData)

# popitem()
userData.popitem()
print(userData)

# pop()
userData.pop("name")
print(userData)


# clear() empty the dictionary

# copty and = same as before

# items()  keys()  values()
print()
print(userData.items())
print()
print(userData.keys())
print()
print(userData.values())
