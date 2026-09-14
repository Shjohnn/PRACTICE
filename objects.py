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
