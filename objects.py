"""
1) what is object in python?
2) Iterable object and range
3) Dictionary 
4)Error handling in python
"""

print("===========What is an Object in Python?===================")

import array
import math
from math import ceil, asin
#everything in Python is an object.
print(type(10))  # <class 'int'>
print(type(10.5))  # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type(True))  # <class 'bool'>


#paradigma > Functional Programming & OOP
#OOP 4 concepts > Abstraction, Encapsulation, Inheritence, Polimorphism

a= 97.8
result1 = math.ceil(a) #call
print(result1)

result2 = ceil(1.1)
print(result2)



print("============Iterable objects===================")

text ="MIT"
for letter in text:
    print(letter)

range_obj= range(3)
for ele in range_obj:
    print(ele)




print("============Dictionary===================")

#Dictionary is JSON object!


person = {"name": "TYLER", "age": 20, "single": True}
person_obj = dict(name="Justin", age=25, single=True)

print(person)
print(person_obj)

name = person_obj["name"]
print(name)

#method:get()

nam= person_obj.get("name")
print("nam:",nam)

balance= person_obj.get("balance",0)
print(balance) # 0 chiqadi

del person_obj['single']
for i in person_obj:
    print(i,person_obj[i])



print("====Error handling system=======")

car_dict = dict(name="toyota", year=2026, electric= True)

try:
    print("try ishladi")
    result2= car_dict['origin']
    a=car_dict.speed
    print(result2)
#Key va Attribute ni bittada handle qilsa boladi
except KeyError as err:
    print("no found")
except AttributeError as err:
    print("attribute error",err)
else:
    print("executed succesfully")
finally:
    print("closing logic")
