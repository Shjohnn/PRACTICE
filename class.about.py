"""
CLASS
1) What is class
2) Ordinary vs static properties
3) Special methods
"""

print("=======What is class==========")

class Person():

    #state
    message='class state property'

    #constructor
    def __init__(self,name, age):
        self.name = name
        self.age = age

    #method
    def introduce(self):
        print(self.name, "says: Salom")

    def say_age(self):
        print(self.name, "is", self.age, "year old" )

    @classmethod
    def explain(cls):
        print("static method property executed")


person1 =Person('Justin', 25)
person2 =Person("Tyler", 20)
person3 =Person("Martin", 30)


person1.introduce()
person2.say_age()




print("======ordinary vs static property==============")

new= Person.message
print(new)

Person.explain()
#static method

