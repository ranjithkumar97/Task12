import json
import mymodule
import datetime

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

a = mymodule.person1["age"]
print(a)


x = datetime.datetime.now()
print(x)


import platform

x = dir(platform)
print(x)