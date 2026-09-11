'''
FUNCTIONS

1) DEFINE VS CALL
2) PARAMETERS AND ARGUMENTS
3) KEYWORD , DEFAULT ARGUMENTS
4. SCOPE
'''


from unicodedata import name


print('======define(parameters) vs call(arguments)================ ')
# built in functions: print(), input(), type(), len() etc
# Functions are defined using the def keyword, followed by the function name and parentheses.
# The function body is indented below the definition.


# defining a function
def greet(name):
    print(f"Hello, {name}!")


def greeting(name):
    return f"Hello, {name}!"


# calling the function
greet("Alice")
result = greeting("Bob")
print(result)  # Output: Hello, Bob!


print('======Keyword vs Default arguments================ ')

#define
def give_greeting(name, age):
    return f"Hello, {name}! You are {age} years old."

give_greeting("Alice", 30)  # Positional arguments
give_greeting(age=30, name="Alice")  # Keyword arguments