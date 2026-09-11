#Dunder __builtins__ , __init__,

message =  'everything is working fine'
print(message)

result = type(message)
print(result)

'''
In Python, there are built-in tools:
1) TYPES > int flooat str list dict set tuple bool complex
2) FUNCTIONS > print() input() len() type() range() sum() min() max() sorted()
3) CONSTANTS > True False None
'''

print(dir(__builtins__))  