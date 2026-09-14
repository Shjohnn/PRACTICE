#Dunder __builtins__ , __init__,

a =  'everything is working fine'
print(a)

result = type(a)
print(result)

'''
In Python, there are built-in tools:
1) TYPES > int flooat str list dict set tuple bool complex
2) FUNCTIONS > print() input() len() type() range() sum() min() max() sorted()
3) CONSTANTS > True False None
'''

print(dir(__builtins__))  