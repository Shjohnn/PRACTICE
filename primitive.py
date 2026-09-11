print('================================ ')

 #in java, varuable is a name storage location, 
 #in python variable is a named reference to an object in memory

count = 10
count_type = type(count)

print(count_type)
print(f"The variable 'count' is of type: {count_type}  ")

result1 = count.bit_count() #method of int class

result2 = count.numerator #state

print(f"result1: {result1}  result2: {result2} ")   



print('=================string=============== ')
#   methods: upper() title() lower() capitalize() count() find() index()  isdigit() isspace() split() join()

course ='AI Python Full Stack'
result3 = type(course)
print(f"The variable 'course' is of type: {result3}  ")
result3=course.title()
result = course.upper()     
print(f"result: {result}  ")
print(f"result3: {result3}  ")
result= course.replace('Python','Java') 
print(f"result: {result}  ")


print('=================boolean=============== ')

# y= input("Enter a number: ")
# print(f"y: {y}  type(y): {type(y)}  ")
# result = y.isnumeric()  #returns True if all characters in the string are numeric
# print(f"result: {result}  ")


#Truthy and Falsy values in Python

#truthy > True
#falsy > False 0 "" None [] {} set() ()

test_falsy  ='' 
print("the falsy: ", bool(test_falsy))  #False

test_truthy = "Hello"
print("the truthy: ", bool(test_truthy))  #True