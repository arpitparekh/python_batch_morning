# api
# application programming interface
# client and server

# "https://www.google.com/search?q=hello"
# "https://www.youtube.com/watch?v=v4H2fTgHGuc"

# url is a way to communicate with the server
# api => json,xml,html

import requests
import json
url = "https://hacker-news.firebaseio.com/v0/item/192327.json"

response= requests.get(url)
# print(response.json())

dictionary = json.loads(response.text)
print(dictionary['title'])
print(dictionary['text'])
